from twilio.rest import Client
def message(content,number):

 account_sid = "ACcec030ceb7f1daf3ea4b43463a53ec82"
 auth_token = "db9b01e0c2959b37891bb358795d8ef2"
 client = Client(account_sid, auth_token)

 message = client.messages \
                .create(
                     body=content,
                     from_='+15673471540',
                     to= number
                 )
