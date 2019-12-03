import smtplib
from email.mime.text import MIMEText

def send_email(msg):
    #smtp server details.
    port = 2525
    smtp_server = 'smtp.mailtrap.io'

    #your authentification.
    login = ''
    password = ''
    
    #email details.
    sender = 'testmail1@mail.com'
    reciever = 'testmail2@mail.com'
    message = MIMEText(msg)
    message['Subject'] = 'delivery notice'
    message['From'] = sender
    message['To'] = reciever

    #send your email.
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, reciever, message.as_string())
