from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twilio credentials
account_sid = 'AC4fbfb996bb846c43c234c28f2429cd37'
auth_token = '18180a51b85af7ffba92000255c661b0'
twilio_phone_number = '+14793780765'

# Your phone number (the recipient)
to_phone_number = '+918150943182'

# Message to send
message_body = 'I am in danger, I need help'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

try:
    # Send the message
    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=to_phone_number
    )
    print(f"Message sent with SID: {message.sid}")
except TwilioRestException as e:
    print(f"Twilio error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
