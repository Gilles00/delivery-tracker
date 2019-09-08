import smtplib
from email.mime.text import MIMEText

def send_email(msg):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '45f79c883f409e'
    password = '44fb7d6564cf0f'
    
    sender = 'testmail1@mail.com'
    reciever = 'testmail2@mail.com'
    message = MIMEText(f'Your package has been {msg}')
    message['Subject'] = 'delivery notice'
    message['From'] = sender
    message['To'] = reciever

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender, reciever, message.as_string())
