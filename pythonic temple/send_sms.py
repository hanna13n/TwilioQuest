from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=os.environ['TWILIO_PHONE_NUMBER'],
    body='Hey Haneen Sadik N, We are from twilio and would like to offer you a free twilio credit. Please reply 1 to redeem your credit.',
    to='+918281131545'
)

print(message.sid)
