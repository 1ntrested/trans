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
account_sid="AC9b341752da2ac1431b4c5543d185d9e5"
auth_token="7c2ee32feecba87d8eb10920d5f5cef5"
client = Client(account_sid, auth_token)
current = {}

@views.route('/')
@login_required
def home():
    return render_template("home.html",current_user=current_user)


@views.route('/transactionprocessing/<dim>', methods=['POST'])
def transactionprocessing(dim):
    res = request.get_json()
    check = dim
    messages(check)
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

def messages(check):

    if check == "2":
        message("The transaction Failed as you voice doesn't match","+917834858496")
    elif check == "3":
        message("The recipients number does not exist","+917834858496")
    elif check == "4":
        message("Rs 100 transferred to 9319962568","+917834858496")
        message("Rs 100 received from to 9319962568","+917834858496")

    else :
        message("An error occured try again Later","+917834858496")
