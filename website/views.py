from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required,current_user
from .models import transactiondetails,User
from . import db
import requests
from .message import  message
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import time

views = Blueprint('views', __name__)

account_sid = "ACcec030ceb7f1daf3ea4b43463a53ec82"
auth_token = "7bbbd761f11355a0051990ae18db5b01"
client = Client(account_sid, auth_token)
current = {}

@views.route('/')
@login_required
def home():
    return render_template("home.html",current_user=current_user)


@views.route('/transactionprocessing', methods=['POST'])
def transactionprocessing():
    res = request.get_json()
    check = res["dim"]
    time.sleep(20)
    if check == "2":
        message("The transaction Failed as you voice doesn't match","+919625336696")
    if check == "3":
        message("The recipients number does not exist","+919625336696")
    if check == "4":
        message("Rs 100 transferred to 8448864282","+919625336696")
        message("Rs 100 received from to 9625336696","+918448864282")
    return res



def download_audio(url, local_filename):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(local_filename, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=128):
                        file.write(chunk)

                print(f"Audio file downloaded successfully: {local_filename}")
            else:
                print(f"Failed to download audio. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

