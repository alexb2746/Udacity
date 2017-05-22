from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC030c466365cceeccdf3d442fd5b3e6c3"
# Your Auth Token from twilio.com/console
auth_token  = "a308f3c3011e39aa5b799d7ef03fbe09"

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+15179174866",
    from_="+15174350320",
    body="Hello from Python!")

print(message.sid)
