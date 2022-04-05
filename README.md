# Mozilla L10n Linter

The scripts in this repository can be used to lint reference files and
localized monorepos, i.e. repositories which include source and localized
resources.

The list of errors for failed runs is available as an artifact (`errors-list`):
* Click on the link in the project column.
* Click on the first failed run (with a red cross) on the right.
* The list of errors will be displayed in the logs. It’s also possible to download the list as a file in the `Artifacts` section at the bottom of the page. For both actions it’s necessary to be logged in to GitHub.

It's possible to define [exceptions](https://github.com/flodolo/mozl10n-linter/tree/main/l10n/exceptions) for specific type of checks in each project.

## Android (XML)

| Project | Linter Status |
|---------|---------------|
|[Firefox for Android](https://github.com/flodolo/mozl10n-linter/actions/workflows/firefox_android.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Firefox%20Android/badge.svg)
|[Focus for Android](https://github.com/flodolo/mozl10n-linter/actions/workflows/focus_android.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Focus%20Android/badge.svg)

## Fluent

| Project | Linter Status |
|---------|---------------|
|[Firefox Accounts](https://github.com/flodolo/mozl10n-linter/actions/workflows/fxa.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/FxA/badge.svg)
|[Firefox Relay](https://github.com/flodolo/mozl10n-linter/actions/workflows/relay.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Relay/badge.svg)
|[Firefox Monitor](https://github.com/flodolo/mozl10n-linter/actions/workflows/monitor.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Monitor/badge.svg)
|[Firefox Profiler](https://github.com/flodolo/mozl10n-linter/actions/workflows/profiler.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Profiler/badge.svg)
|[mozilla.org](https://github.com/flodolo/mozl10n-linter/actions/workflows/mozorg.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/MozOrg/badge.svg)

## JSON (WebExtensions)
| Project | Linter Status |
|---------|---------------|
|[Firefox Multi-Account Containers](https://github.com/flodolo/mozl10n-linter/actions/workflows/mac.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/MAC/badge.svg)
|[Firefox Relay Add-on](https://github.com/flodolo/mozl10n-linter/actions/workflows/relay_addon.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Relay%20Add-on/badge.svg)
|[Firefox Translations](https://github.com/flodolo/mozl10n-linter/actions/workflows/translations.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Translations/badge.svg)

## XLIFF (iOS, qt)
| Project | Linter Status |
|---------|---------------|
|[Firefox for iOS](https://github.com/flodolo/mozl10n-linter/actions/workflows/firefox_ios.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Firefox%20iOS/badge.svg)
|[Focus for iOS](https://github.com/flodolo/mozl10n-linter/actions/workflows/focus_ios.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/Focus%20iOS/badge.svg)
|[Mozilla VPN Client](https://github.com/flodolo/mozl10n-linter/actions/workflows/vpn.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/VPN%20Client/badge.svg)

## Gettext
| Project | Linter Status |
|---------|---------------|
|[Firefox Accounts](https://github.com/flodolo/mozl10n-linter/actions/workflows/fxa_gettext.yaml)|![Linter status](https://github.com/flodolo/mozl10n-linter/workflows/FxA%20Gettext/badge.svg)
