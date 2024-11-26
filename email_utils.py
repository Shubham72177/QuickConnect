import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender_email, sender_password, recipient_email, name, company_name, resume_path):
    try:
        # Create email
        subject = f"Excited to Explore Opportunities at {company_name}"
        body = f"""
        Dear {company_name},

        My name is {name}, and I came across your company while exploring opportunities in my domain.
        I am impressed by the work {company_name} is doing and would love the opportunity to contribute.

        I have attached my resume for your reference and look forward to hearing from you.

        Best regards,
        {name}
        """

        # Email setup
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Attach resume
        with open(resume_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(resume_path)}")
        message.attach(part)

        # Send email using SMTP
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())

    except Exception as e:
        raise e
