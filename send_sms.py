from twilio.rest import Client

def sendMessage(toNumber, fromNumber, message):
    account_sid = "AC9b64644cb7c33ef1467ab5fba7aa385f"

    auth_token  = "b88f5ffb3a8fe815538506ebed83b3d6"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to = toNumber,
        from_ = fromNumber,
        body = message)

#sendMessage("7853200582", "7165314545", "Hey Tony")
