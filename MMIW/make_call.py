# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfa70159643cbb4d89cbfbbc3fb4e5a92'
auth_token = '3cb1fe7285f883d286682cabcee5faef'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+18187915011',
                        from_='+12563056154'
                    )

print(call.sid)
