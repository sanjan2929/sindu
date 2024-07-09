from twilio.rest import Client

account_sid = 'AC4fbfb996bb846c43c234c28f2429cd37'
auth_token = '18180a51b85af7ffba92000255c661b0'
twilio_phone_number = '+14793780765'

# The recipient's phone number
to_phone_number = '+918150943182'

# TwiML URL containing the message
twiml_url = 'https://handler.twilio.com/twiml/EH31d7b98052a5d336dbc4b3d6b0589bd1'  # Replace with your TwiML URL

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=to_phone_number,
    from_=twilio_phone_number,
    url=twiml_url
)

print(f"Call initiated with SID: {call.sid}")
