#! /usr/bin/env python3

import argparse
import requests
import smtplib
from collections import defaultdict
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password, server, port):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = f"L10n Automation <{sender}>"
    msg["To"] = ", ".join(recipients)
    smtp_server = smtplib.SMTP_SSL(server, port)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--api", required=True, dest="api_token", help="GitHub API Token"
    )
    parser.add_argument(
        "--server",
        required=False,
        dest="smtp_server",
        default="smtp.gmail.com",
        help="SMTP URL",
    )
    parser.add_argument(
        "--port", required=False, dest="smtp_port", default="465", help="SMTP URL"
    )
    parser.add_argument(
        "--user", required=True, dest="smtp_user", help="Username for SMTP server"
    )
    parser.add_argument(
        "--password",
        required=True,
        dest="smtp_password",
        help="Password for SMTP server",
    )
    args = parser.parse_args()

    workflows = {
        "firefox_android": "dlebedel",
        "firefox_ios": "dlebedel",
        "focus_android": "dlebedel",
        "focus_ios": "dlebedel",
        "fxa": "bolsson",
        "fxa_gettext": "bolsson",
        "mac": "flodolo",
        "monitor": "flodolo",
        "mozorg": "pmo",
        "pocket": "pmo",
        "profiler": "flodolo",
        "relay": "pmo",
        "relay_addon": "pmo",
        "translations": "flodolo",
        "vpn": "flodolo",
    }

    url = "https://api.github.com/repos/mozilla-l10n/mozl10n-linter/actions/workflows/{}.yaml/runs"
    headers = {"Authorization": f"token {args.api_token}"}

    failures = defaultdict(list)
    for w, owner in workflows.items():
        url_workflow = url.format(w)
        r = requests.get(url=url_workflow, headers=headers)
        last_run = r.json()["workflow_runs"][0]
        if last_run["conclusion"] == "failure":
            failures[owner].append(
                {
                    "name": last_run["display_title"],
                    "url": last_run["html_url"],
                }
            )

    if failures:
        for owner, owner_failures in failures.items():
            output = ["There are failures in the following projects:"]
            recipients = [f"{owner}+l10nlint@mozilla.com"]
            subject = "Failures in Mozilla L10n Linters"
            for failure in owner_failures:
                output.append(f"- {failure['name']}: {failure['url']}")
            body = "\n".join(output)

            print(f"Sending email to {','.join(recipients)}")
            send_email(
                subject,
                body,
                args.smtp_user,
                recipients,
                args.smtp_password,
                args.smtp_server,
                args.smtp_port,
            )


if __name__ == "__main__":
    main()
