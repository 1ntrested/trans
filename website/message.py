from twilio.rest import Client
def message(content,number):
    account_sid="AC9b341752da2ac1431b4c5543d185d9e5"
    auth_token="7c2ee32feecba87d8eb10920d5f5cef5"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=content,
                        from_='+15203143474',
                        to= number
                    )

