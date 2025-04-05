from twilio.rest import Client

account_sid = 'your_account_sid'  
auth_token = 'your_auth_token'   

# Create a Twilio client
client = Client(account_sid, auth_token)

# Sending an SMS
message = client.messages.create(
    body='Hello! This is a test message from Python.',  
    from_='+1234567890',  
    to='+0987654321'      
)

print(f"Message sent with SID: {message.sid}")
