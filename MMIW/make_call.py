#SIM
from twilio.rest import Client



account_sid = 'ACfa70159643cbb4d89cbfbbc3fb4e5a92'
auth_token = '3cb1fe7285f883d286682cabcee5faef'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://2f9087b3.ngrok.io/',
                        to='+18187915011',
                        from_='+12563056154'
                    )

print(call.sid)
