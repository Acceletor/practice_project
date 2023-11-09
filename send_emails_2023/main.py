import os
from email.message import EmailMessage
import ssl # standard technology to keep internet connection secure and afeguarding the data that being sent btw two systems
import smtplib # to send email

email_sender = os.environ.get("EMAIL")
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = os.environ.get("EMAIL_RECEIVER")

subject = "SUBJECT OF THE EMAIL"
body = """
This is for testing purpose!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# for security
context = ssl.create_default_context()

# define email server, port, and context
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context) as smtp:
    #login
    smtp.login(email_sender,email_password)
    # define sender, receiver, and context
    smtp.sendmail(email_sender, email_receiver, em.as_string())