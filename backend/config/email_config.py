from email.message import EmailMessage
import smtplib

sender_email = "my_email@example.com"
password = "my_password"
receiver_email = "your_email@example.com"
Server="smtp.gmail.com"
Port=465

def send_alert(sender_email, password, receiver_email,Server,Port):
    msg=EmailMessage()
    Subject="Alert Occured"
    Body="An alert has been triggered and needs to be fixed immediately."
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']=Subject
    msg.set_content(Body)

    with smtplib.SMTP_SSL(Server,Port) as smtp:
        smtp.login(sender_email,password)
        smtp.send_message(msg)