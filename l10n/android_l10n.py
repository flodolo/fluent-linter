#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from collections import defaultdict, Counter
from custom_html_parser import MyHTMLParser
import argparse
import json
import os
import re
import sys

try:
    from compare_locales import paths
    from compare_locales import parser
except ImportError as e:
    print("FATAL: make sure that dependencies are installed")
    print(e)
    sys.exit(1)


class StringExtraction:
    def __init__(self, l10n_path, reference_locale):
        """Initialize object."""

        self.translations = defaultdict(dict)

        self.l10n_path = l10n_path
        self.reference_locale = reference_locale

    def extractStringsToml(self):
        """Extract strings using TOML configuration."""

        basedir = os.path.dirname(self.l10n_path)
        project_config = paths.TOMLParser().parse(self.l10n_path, env={"l10n_base": ""})
        basedir = os.path.join(basedir, project_config.root)

        reference_cache = {}

        if not project_config.all_locales:
            print("No locales defined in the project configuration.")

        for locale in project_config.all_locales:
            print(f"Extracting strings for locale: {locale}.")
            files = paths.ProjectFiles(locale, [project_config])

            for l10n_file, reference_file, _, _ in files:
                if not os.path.exists(l10n_file):
                    # File not available in localization
                    continue

                if not os.path.exists(reference_file):
                    # File not available in reference
                    continue

                key_path = os.path.relpath(reference_file, basedir)
                try:
                    p = parser.getParser(reference_file)
                except UserWarning:
                    continue
                if key_path not in reference_cache:
                    p.readFile(reference_file)
                    reference_cache[key_path] = set(p.parse().keys())
                    self.translations[self.reference_locale].update(
                        (
                            f"{key_path}:{entity.key}",
                            entity.raw_val,
                        )
                        for entity in p.parse()
                    )

                p.readFile(l10n_file)
                self.translations[locale].update(
                    (
                        f"{key_path}:{entity.key}",
                        entity.raw_val,
                    )
                    for entity in p.parse()
                )
            print(f"  {len(self.translations[locale])} strings extracted")

    def extractStrings(self):
        """Extract strings from all locales."""

        self.extractStringsToml()

    def getTranslations(self):
        """Return dictionary with translations"""

        return self.translations


class QualityCheck:
    def __init__(self, translations, reference_locale, exceptions_path):

        self.translations = translations
        self.reference_locale = reference_locale
        self.exceptions_path = exceptions_path
        self.error_messages = defaultdict(list)

        self.runChecks()

    def runChecks(self):
        """Check translations for issues"""

        def ignoreString(exceptions, locale, errorcode, string_id):
            """Check if a string should be ignored"""

            if not exceptions:
                return False

            if errorcode == "ellipsis":
                if locale in exceptions[errorcode][
                    "excluded_locales"
                ] or string_id in exceptions[errorcode]["locales"].get(locale, {}):
                    return True
            else:
                # Ignore excluded strings
                if string_id in exceptions[errorcode]["strings"]:
                    return True
                if (
                    locale in exceptions[errorcode]["locales"]
                    and string_id in exceptions[errorcode]["locales"][locale]
                ):
                    return True

            return False

        placeable_pattern = re.compile(r"((%)(?:[0-9]+\$){0,1}([sd]))")

        # Load exceptions
        if not self.exceptions_path:
            exceptions = {}
        else:
            try:
                with open(self.exceptions_path) as f:
                    exceptions = json.load(f)
            except Exception as e:
                sys.exit(e)

        """
        Store specific reference strings for addictional FTL checks:
        - Strings with data-l10n-names
        - Strings with message, terms, or variable references
        """
        reference_data = self.translations[self.reference_locale]
        placeable_ids = {}
        for string_id, text in reference_data.items():
            file_id, message_id = string_id.split(":")

            if not isinstance(text, str):
                continue

            matches_iterator = placeable_pattern.finditer(text)
            matches = defaultdict(list)
            for m in matches_iterator:
                matches["original"].append(m.group(1))
                if len(m.group()) > 3:
                    # String is using ordered placeables
                    matches["unordered"].append(m.group(2) + m.group(3))
                else:
                    # String is already using unordered placeables
                    matches["unordered"].append(m.group(1))
            if matches:
                placeable_ids[string_id] = {
                    "original": sorted(matches["original"]),
                    "unordered": matches["unordered"],
                }

        # Store strings with HTML elements
        html_parser = MyHTMLParser()
        html_strings = {}
        for string_id, text in reference_data.items():
            if not isinstance(text, str):
                continue

            html_parser.clear()
            html_parser.feed(text)

            tags = html_parser.get_tags()
            if tags:
                html_strings[string_id] = tags

        for locale, locale_translations in self.translations.items():
            # Ignore reference locale
            if locale == self.reference_locale:
                continue

            # General checks on localized strings
            for string_id, translation in locale_translations.items():
                # Ignore excluded strings
                if ignoreString(exceptions, locale, "general", string_id):
                    continue

                translation = locale_translations[string_id]
                if not isinstance(translation, str):
                    continue

                # Ignore if it's an obsolete translation not available in the
                # reference file.
                if string_id not in self.translations[self.reference_locale]:
                    continue
                reference = self.translations[self.reference_locale][string_id]

                # Check for pilcrow character
                if "¶" in translation:
                    error_msg = (
                        f"'¶' in {string_id}\n"
                        f"  Translation: {translation}\n"
                        f"  Reference: {reference}"
                    )
                    self.error_messages[locale].append(error_msg)

                # Check for empty translation
                if translation == "":
                    error_msg = (
                        f"{string_id} is empty\n"
                        f"  Translation: {translation}\n"
                        f"  Reference: {reference}"
                    )
                    self.error_messages[locale].append(error_msg)

                # Check for 3 dots instead of ellipsis
                if "..." in translation and not ignoreString(
                    exceptions, locale, "ellipsis", string_id
                ):
                    error_msg = (
                        f"'...' in {string_id}\n"
                        f"  Translation: {translation}\n"
                        f"  Reference: {reference}"
                    )
                    self.error_messages[locale].append(error_msg)

            # Check all localized strings for HTML elements mismatch or extra tags
            html_parser = MyHTMLParser()
            for string_id, translation in locale_translations.items():
                # Ignore excluded strings
                if ignoreString(exceptions, locale, "HTML", string_id):
                    continue

                translation = locale_translations[string_id]
                if not isinstance(translation, str):
                    continue

                html_parser.clear()
                html_parser.feed(translation)
                tags = html_parser.get_tags()

                ref_tags = html_strings.get(string_id, [])
                if tags != ref_tags:
                    # Ignore if only the order was changed
                    if sorted(tags) == sorted(ref_tags):
                        continue

                    # Check extra or missing tags and ignore the error if it's
                    # only <i> and <em>, and the number of extra tags is even.
                    tags_diff = list(Counter(tags) - Counter(ref_tags)) + list(
                        Counter(ref_tags) - Counter(tags)
                    )
                    diff_list = [
                        t
                        for t in tags_diff
                        if t not in ["<em>", "</em>", "<i>", "</i>"]
                    ]
                    if not diff_list and (len(tags_diff) % 2) == 0:
                        continue

                    error_msg = (
                        f"Mismatched HTML elements in string ({string_id})\n"
                        f"  Translation tags ({len(tags)}): {', '.join(tags)}\n"
                        f"  Reference tags ({len(ref_tags)}): {', '.join(ref_tags)}\n"
                        f"  Translation: {translation}\n"
                        f"  Reference: {self.translations[self.reference_locale][string_id]}"
                    )
                    self.error_messages[locale].append(error_msg)

            # Check placeables
            for string_id, groups in placeable_ids.items():
                if string_id not in locale_translations:
                    continue

                # Ignore excluded strings
                if ignoreString(exceptions, locale, "placeables", string_id):
                    continue

                translation = locale_translations[string_id]
                if not isinstance(translation, str):
                    continue
                matches_iterator = placeable_pattern.finditer(translation)
                matches = defaultdict(list)
                for m in matches_iterator:
                    matches["original"].append(m.group(1))
                    if len(m.group()) > 3:
                        # String is using ordered placeables
                        matches["unordered"].append(m.group(2) + m.group(3))
                    else:
                        # String is already using unordered placeables
                        matches["unordered"].append(m.group(1))

                if matches:
                    translated_groups = sorted(matches["original"])
                    if translated_groups != groups["original"]:
                        # Groups are not matching, but the translation might be
                        # using ordered placeables instead of unordered, or
                        # the other way around.
                        # "%1$s" would be stored as "%s" in the "unordered"
                        # array.
                        if matches["unordered"] == groups["unordered"]:
                            continue
                        error_msg = (
                            f"Placeable mismatch in string ({string_id})\n"
                            f"  Translation: {translation}\n"
                            f"  Reference: {self.translations[self.reference_locale][string_id]}"
                        )
                        self.error_messages[locale].append(error_msg)
                else:
                    # There are no data-l10n-name
                    error_msg = (
                        f"Placeable missing in string ({string_id})\n"
                        f"  Translation: {translation}\n"
                        f"  Reference: {self.translations[self.reference_locale][string_id]}"
                    )
                    self.error_messages[locale].append(error_msg)

    def printErrors(self):
        """Print error messages"""

        output = []
        total = 0
        if self.error_messages:
            locales = list(self.error_messages.keys())
            locales.sort()

            for locale in locales:
                output.append(
                    f"\nLocale: {locale} ({len(self.error_messages[locale])})"
                )
                total += len(self.error_messages[locale])
                for e in self.error_messages[locale]:
                    output.append(f"\n  {e}")

            output.append(f"\nTotal errors: {total}")

        return output


def main():
    # Read command line input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--toml", required=True, dest="toml_path", help="Path to l10n.toml file"
    )
    parser.add_argument("--ref", dest="reference_code", help="Reference language code")
    parser.add_argument("--dest", dest="dest_file", help="Save output to file")
    parser.add_argument(
        "--exceptions",
        nargs="?",
        dest="exceptions_file",
        help="Path to JSON exceptions file",
    )
    args = parser.parse_args()

    extracted_strings = StringExtraction(
        l10n_path=args.toml_path,
        reference_locale=args.reference_code,
    )
    extracted_strings.extractStrings()
    translations = extracted_strings.getTranslations()

    checks = QualityCheck(translations, args.reference_code, args.exceptions_file)
    output = checks.printErrors()
    if output:
        out_file = args.dest_file
        if out_file:
            print(f"Saving output to {out_file}")
            with open(out_file, "w") as f:
                f.write("\n".join(output))
        # Print errors anyway on screen
        print("\n".join(output))
        sys.exit(1)
    else:
        print("No issues found.")


if __name__ == "__main__":
    main()
