from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    phone = db.Column(db.String(11),unique = True)
    name = db.Column(db.String(150))
    pin = db.Column(db.String(5))
    balance = db.column(db.String(150))
    history = db.relationship('transactiondetails')


class transactiondetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Transaction_Details = db.Column(db.String(150))
    dandt = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# class WaitList(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150),unique = True)
#     password = db.Column(db.String(150))
#     phone = db.Column(db.String(11),unique = True)
#     name = db.Column(db.String(150))
#     pin = db.Column(db.String(5))
#     balance = db.column(db.String(150))

