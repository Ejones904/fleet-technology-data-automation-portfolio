import os
import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# ============================================================
# EMAIL CONFIGURATION
#
# Public portfolio modification:
# Original email address and application password removed.
# Credentials are now loaded from environment variables.
# ============================================================

sender_email = os.getenv("SMTP_USERNAME")
sender_password = os.getenv("SMTP_PASSWORD")

smtp_server = "smtp.gmail.com"
smtp_port = 587


# ============================================================
# LOAD CASE DATA
#
# Original workstation path and production spreadsheet removed.
# Public version uses synthetic sample data.
# ============================================================

case_data = pd.read_excel(
    "sample-data/cases.xlsx"
)


# ============================================================
# PROCESS CASE RECORDS
# ============================================================

for index, row in case_data.iterrows():

    recipient_email = row["Email"]
    recipient_name = row["Name"]
    case_number = row["Case_Number"]
    case_description = row["Case_Description"]


    # ========================================================
    # CREATE PERSONALIZED EMAIL
    # ========================================================

    subject = f"Follow Up - Case {case_number}"

    body = f"""
Hello {recipient_name},

I am following up regarding case {case_number}.

Case Description:
{case_description}

Please let me know if the issue has been resolved or if
additional assistance is needed.

Thank you.
"""


    # ========================================================
    # BUILD MIME MESSAGE
    # ========================================================

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain")
    )


    # ========================================================
    # SEND EMAIL
    # ========================================================

    try:

        server = smtplib.SMTP(
            smtp_server,
            smtp_port
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            recipient_email,
            message.as_string()
        )

        server.quit()

        print(
            f"Follow-up sent for case {case_number}"
        )

    except Exception as error:

        print(
            f"Unable to send follow-up for "
            f"case {case_number}: {error}"
        )
