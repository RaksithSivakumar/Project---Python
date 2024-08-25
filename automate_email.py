import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
USERNAME = 'your-email@gmail.com'
PASSWORD = 'your-password'

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  
        server.login(USERNAME, PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        
        server.quit()

if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a test email sent from Python!"
    to_email = "recipient@example.com"
    send_email(subject, body, to_email)
