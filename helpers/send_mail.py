import smtplib


def send_email(user, pwd, recipient, subject, body):
    # Prepare actual message
    message = (
        "From: {0}\n"
        "To: {1}\n"
        "subject: {2}\n\n"
        "{3}"
    ).format(user, recipient, subject, body)

    # connect to smtp.gamil.com:587
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # put the SMTP connection in TLS (Transport Layer Security) mode
    server.starttls()
    server.login(user, pwd)

    server.sendmail(user, recipient, message)
    server.close()
