from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0fb924403cb65b49c70ec2b0e60aceca"
# Your Auth Token from twilio.com/console
auth_token  = "f0159e724e0a30552e6637fd87639615"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18786111008",# Your Phone Number
    from_="+12568294346",# Your Twilio Number
    body="Hello from Python!")

print(message.sid)

