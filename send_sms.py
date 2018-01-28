from twilio.rest import Client

def URL(url):
    return url
account_sid = "AC9b64644cb7c33ef1467ab5fba7aa385f"

auth_token  = "b88f5ffb3a8fe815538506ebed83b3d6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to = "+17853805890",
    from_ = "+17165314545",
    body = URL(url))

print(message.sid)