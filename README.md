# Mozilla L10n Linter

The scripts in this repository can be used to lint reference files and
localized monorepos, i.e. repositories which include source and localized
resources.

The list of errors for failed runs is available as an artifact (`errors-list`):
* Click on the link in the project column.
* Click on the first failed run (with a red cross) on the right.
* The list of errors will be displayed in the logs. It’s also possible to download the list as a file in the `Artifacts` section at the bottom of the page. For both actions it’s necessary to be logged in to GitHub.

It's possible to define [exceptions](https://github.com/mozilla-l10n/mozl10n-linter/tree/main/l10n/exceptions) for specific type of checks in each project.

## Android (XML)

| Project | Linter Status |
|---------|---------------|
|[Firefox for Android](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/firefox_android.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Firefox%20Android/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/firefox_android.yaml)
|[Focus for Android](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/focus_android.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Focus%20Android/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/focus_android.yaml)

## Fluent

| Project | Linter Status |
|---------|---------------|
|[Firefox Accounts](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/fxa.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/FxA/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/fxa.yaml)
|[Firefox Relay](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/relay.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Relay/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/relay.yaml)
|[Firefox Monitor](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/monitor.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Monitor/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/monitor.yaml)
|[Firefox Profiler](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/profiler.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Profiler/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/profiler.yaml)
|[mozilla.org](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/mozorg.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/MozOrg/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/mozorg.yaml)
|[Pocket Marketing Pages](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/pocket.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Pocket%20Marketing%20Pages/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/pocket.yaml)

## JSON (WebExtensions)
| Project | Linter Status |
|---------|---------------|
|[Firefox Multi-Account Containers](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/mac.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/MAC/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/mac.yaml)
|[Firefox Relay Add-on](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/relay_addon.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Relay%20Add-on/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/relay_addon.yaml)
|[Firefox Translations](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/translations.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Translations/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/translations.yaml)

## XLIFF (iOS, qt)
| Project | Linter Status |
|---------|---------------|
|[Firefox for iOS](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/firefox_ios.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Firefox%20iOS/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/firefox_ios.yaml)
|[Focus for iOS](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/focus_ios.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/Focus%20iOS/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/focus_ios.yaml)
|[Mozilla VPN Client](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/vpn.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/VPN%20Client/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/vpn.yaml)

## Gettext
| Project | Linter Status |
|---------|---------------|
|[Firefox Accounts](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/fxa_gettext.yaml)|[![Linter status](https://github.com/mozilla-l10n/mozl10n-linter/workflows/FxA%20Gettext/badge.svg)](https://github.com/mozilla-l10n/mozl10n-linter/actions/workflows/fxa_gettext.yaml)
