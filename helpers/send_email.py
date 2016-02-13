import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(user, pwd, recipient, subject, body):
    # Prepare actual message
    message = (
        'From: {0}\n'
        'To: {1}\n'
        'subject: {2}\n\n'
        '{3}'
    ).format(user, recipient, subject, body)

    message = MIMEMultipart('alternative')
    message['subject'] = subject
    message['To'] = recipient
    message['From'] = user

    html_body = MIMEText(body, 'html')
    message.attach(html_body)

    # connect to smtp.gamil.com:587
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # put the SMTP connection in TLS (Transport Layer Security) mode
    server.starttls()
    server.login(user, pwd)

    server.sendmail(user, recipient, message.as_string())
    server.close()
