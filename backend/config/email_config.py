from email.message import EmailMessage
import smtplib

sender_email = "aaront.bca2428@saintgits.org"
password = "pwza lohg msnb nhmj"
receiver_email = "aaront.bca2428@saintgits.org"
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
send_alert(sender_email, password, receiver_email,Server,Port)

'''import smtplib

def send_email(sender_email, receiver_email, password):

    smtp_server = "smtp.gmail.com" #smtp server is a server that is used to send email . 
    smtp_port = 587

    subject = "Test Email"
    body = "Hello "

    # Create simple email text
    message = f"Subject: {subject}\n\n{body}"

    try:
        print("Connecting to SMTP server...")
        server = smtplib.SMTP(smtp_server, smtp_port)

        print("Starting secure connection...")
        server.starttls()

        print("Logging in...")
        server.login(sender_email, password)

        print("Sending email...")
        server.sendmail(sender_email, receiver_email, message)

        print("Email sent successfully!")

        server.quit()

    except Exception as e:
        print("Error:", e)

# Example usage
send_email(
    sender_email="",
    receiver_email="",
    password=""
)'''


#what is port number: port number that tells to the computer which server  or application should recive  the data .
#example: buliding address  -->IP address {system} 
#flat number --> port number {application}
#delivery boy --> data packets 
# IN computer terms ---> one computer run many services or applications at the same time , either websites or emails or any other file transfers
# All use same IP address but different port numbers .
# Some Port Numbers Used For : 
#1.80 for HTTP (web traffic)
#2.443 for HTTPS (secure web traffic)
#3.25 for SMTP (email sending) { old pport number for email sending }
#4.587 for SMTP (email sending with encryption) { new port number for email sending },  25, 587 465  these three are used for email sending and 587 , 467 these two are new port numbers for email sending , 25 is not secure 
#5.110 for POP3 (email receiving) 25 is only for sending email
#6.143 for IMAP (email receiving)
#why we use port number: 
#1)process to process communication
#2)port number is a unique identifier for a  network
#3)enable communication between devices
#4)it specifies server address 
#  5)port number are also used for avoid confusion between different services running on the same machine.
#
#status code:  status code is a three digit number that is sent by the server to the client in response to a request made by the client. It indicates the status of the request and whether it was successful or not.
# status codes are numbers that tells as what happend when a request meet to the server .
#how it works: when you open a website your browser send a request to the server then server responds withh the status code.
#200 OK :successful request {200 series 200 to 299}.
#why 100 , 300, 400 series {Task}.
#smtplib : it is library which is used to connect gmail with smtp server.
#starttls() : it is used to start a secure connection with the server.{server.starttls(sender , password) }.