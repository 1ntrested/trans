import random

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,WaitList
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user
from website.message import message

auth = Blueprint('auth', __name__)
temp = {}

@auth.route('/login',methods = ['GET','POST'])
def login():

    if request.method == "POST":
        phone = request.form.get('phone')
        password = request.form.get('password')

        user = User.query.filter_by(phone=phone).first()

        if user:
            if check_password_hash(user.password,password):
                flash("Logged in successfully ",category="success")
                login_user(user,remember = True)
                del temp[has]
                return redirect(url_for("views.home"))
            else:
               flash("Incorrect password",category="error")
        else:
           flash("email does not exist",category="error")



    return render_template("login.html")


@auth.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == "POST":

        email = request.form.get("email")
        phone = request.form.get("phone")
        name = request.form.get("name")
        pin = request.form.get("pin")
        password = request.form.get("password")
        print(pin,password,name,phone,email)

        if len(phone) < 10 or not phone.isdigit() :
            flash("Invalid phone number",category="error")
        elif len(password) < 7:
             flash("Password too short",category="error")
        elif len(name) < 2 :
            flash("Name must be greater than 1 char !!",category="error")
        elif len(pin) != 4 or not pin.isdigit() :
            flash("Invalid Pin !!",category="error")
        else:
          user = User.query.filter_by(phone=phone).first()
          if not user:
            balance = random.randint(1000,10000)
            otp = random.randint(1000,9999)
            new_user = User(email=email,name=name,phone=phone,balance=balance,password=generate_password_hash(password),pin=generate_password_hash(pin))
            has = str(generate_password_hash(phone))
            message(f"Your otp is {otp}","+919625336696")
            temp[has] = [new_user,otp]
            red = "verify/"+has
            return redirect(red)
          else:
             flash("email already exists",category="error")

    return render_template("signup.html")

@auth.route('/verify/<has>',methods=["GET","POST"])
def verify(has):
    if request.method=="POST":
        otp = request.form.get("otp")

        if int(otp) == int(temp[has][1]):
            flash("Account has been added Kindly complete Your KYC")
            new_user = temp[has][0]
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            id = current_user.id
            return redirect(url_for("views.home"))
            return redirect(url_for("auth.login"))
            flash("Account Created now kindly complete kyc", category="success")
    return render_template("verify.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("logout successful",category="success")
    return redirect(url_for("auth.login"))