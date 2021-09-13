import smtplib


def send_mail(receiver, subject, body, **kwargs):
    """Sends an e-mail from a given e-mail address.
    The receiver, subject and the body are customizable.

    Args:
        receiver (str): e-mail address to the receiver,
        subject (str): title of the e-mail,
        body (str): the text that should be included in the e-mail.

        kwargs: there should be two information passed:
            1. SENDER_MAIL (str): sender's e-mail,
            2. SENDER_PASS (str): sender's e-mail password.
    """
    email_text = """
    From: {sender}
    To: {receiver}
    Subject: {subject}

    {body}
    """.format(sender=kwargs['SENDER_MAIL'], receiver=receiver, subject=subject, body=body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        try:
            server.login(kwargs['SENDER_MAIL'], kwargs['SENDER_PASS'])
            server.sendmail(kwargs['SENDER_MAIL'], receiver, email_text)
            print("Email sent successfully!")
        except Exception as err:
            print("Something went wrong….", err)


if __name__ == "__main__":
    sender = {
        'SENDER_MAIL': 'sender@example.com',
        'SENDER_PASS': 'senders_secret_password'
    }
    send_mail(
        'receiver@example.com',
        'Test e-mail',
        'This is the test',
        sender
    )
