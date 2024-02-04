import time
import requests
from flask import Flask, request
from twilio.twiml.voice_response import Gather, VoiceResponse
from twilio.rest import Client

app = Flask(__name__)
user_data = {}
dim = 0


@app.route('/webhook', methods=['POST'])
def webhook():
    response = VoiceResponse()

    with response.gather(numDigits=1, action='/handle-choice', method='POST') as gather:
        gather.say("press a key to run")

    return str(response)


@app.route('/handle-choice', methods=['POST'])
def handle_choice():
    choice = request.form['Digits']
    response = VoiceResponse()
    global dim
    dim = choice

    if choice == '1':
        response.say("this number does not exist")
    else:
        response.record(action='/handle-recording', maxLength=30, playBeep=True)
        with response.gather(input='speech', action='/handle-recording', method='POST', timeout=10) as gather:
            gather.say("Please say the amount and recipient's phone number.")

    return str(response)


@app.route('/handle-recording', methods=['POST'])
def handle_recording():
    recording_url = request.form['RecordingUrl']
    response = VoiceResponse()

    response.say("You said")
    response.play(recording_url)
    with response.gather(numDigits=5, action='/handle-pin', method='POST') as gather:
            gather.say("Enter your 4-digit PIN.")

    return str(response)


@app.route('/handle-pin', methods=['POST'])
def handle_pin():
    pin = request.form['Digits']
    response = VoiceResponse()
    print(pin)
    if len(pin) == 4:
        user_data['pin'] = pin
        global dim
        data = {"dim": dim}
        url = "tanmayexe123.pythonanywhere.com/transactionprocessing"
        res = requests.post(url, data=data)
    return str(response)




if __name__ == '__main__':
    app.run(debug=True)
