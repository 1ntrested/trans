from twilio.rest import Client
def message(content,number):

 account_sid = "ACcec030ceb7f1daf3ea4b43463a53ec82"
 auth_token = "bd2d64f90243f7c4a0052cce3af47945"
 client = Client(account_sid, auth_token)

 message = client.messages \
                .create(
                     body=content,
                     from_='+15673471540',
                     to= number
                 )
