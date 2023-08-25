import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from typing import List
from dotenv import load_dotenv
load_dotenv()

# Email configuration
sender_email_id = os.environ.get("sender_email_id")
smtp_host = os.environ.get("smtp_host")
smtp_port = os.environ.get("smtp_port")
smtp_username = os.environ.get("smtp_username")
smtp_password = os.environ.get("smtp_password")


def send_email_with_attachment(recipients, attachment_path):
    body = """
    I hope this email finds you well. We are pleased to provide you with your personalized insurance details in the attached PDF document. This document contains all the information you've provided to us for your insurance policy.

    Please review the information carefully and ensure that all the details are accurate. If everything looks correct, all that's left for you to do is add your signature to the designated area. Your signature will confirm your acceptance of the policy terms and complete the application process.

    If you have any questions or if you notice any discrepancies, please don't hesitate to reach out to me. I'm here to assist you every step of the way.

    Thank you for choosing us for your insurance needs. Your satisfaction and security are our top priorities.

    Warm regards,
    goML
    LLM marketplace - policy generator
    """

    subject="Your Personalized Insurance Details - Please Review"
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email_id
        msg["To"] = recipients
        msg["Subject"] = "Your Personalized Insurance Details - Please Review"

        msg.attach(MIMEText(body, "plain"))

        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            msg.attach(part)

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()

        # Log in to your account
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email_id, recipients, msg.as_string())

        # Quit the server
        server.quit()

        print("Email with attachment sent successfully.")
        return 1
    except Exception as e:
        print(e)
        return e
