from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twilio credentials
account_sid = 'ACfcbf372bdfa7dc6abf6d613cc4d63acc'
auth_token = 'f98e0cbfbf82a957ea1011677b4ff93b'
twilio_phone_number = '+15734636566'

# Your phone number (the recipient)
to_phone_number = '+918317361040'

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
