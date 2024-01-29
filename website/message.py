from twilio.rest import Client
def message(content,number):

 account_sid = "ACcec030ceb7f1daf3ea4b43463a53ec82"
 auth_token = "7bbbd761f11355a0051990ae18db5b01"
 client = Client(account_sid, auth_token)

 message = client.messages \
                .create(
                     body=content,
                     from_='+15673471540',
                     to= number
                 )
