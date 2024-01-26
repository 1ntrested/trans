from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    phone = db.Column(db.String(11))
    name = db.Column(db.String(150))
    pin = db.Column(db.String(5))
    balance = db.column(db.string(150))
    history = db.relationship('transactiondetails')


class transactiondetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(1000))
    emerphone = db.Column(db.String(100))
    aadharno = db.Column(db.String(100))
    bloodgroup = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    disease = db.Column(db.String(100))
    allergies = db.Column(db.String(100))
    age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


