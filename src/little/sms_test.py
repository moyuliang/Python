from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxca"
# Your Auth Token from twilio.com/console
auth_token  = "f0xxxxxxxxxxxxxxxxxxxxxxxxxxxx15"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+86xxxxxxxxxxx",# Your Phone Number
    from_="+xxxxxxxxxxx",# Your Twilio Number
    body="Hello from Python!")

print(message.sid)

