from flask import Flask, request
import requests
import json
from pprint import pprint

config_file = open('../config.json', 'r')
config = json.load(config_file)

ACCOUNT_SID = config['account_sid']
AUTH_TOKEN = config['auth_token']

app = Flask(__name__)

numbers = ['+15857977879', '+14154508142']
@app.route('/sms', methods=['POST', 'GET'])
def sms():
    number = request.values.get('From')
    if number in numbers:
        return """<?xml version="1.0" encoding="UTF-8"?>
             <Response>
                 <Sms>Enroll IN THE ESPP!!</Sms>
             </Response>"""
    else:
        return """<?xml version="1.0" encoding="UTF-8"?>
             <Response>
                 <Sms>SORRY, not around</Sms>
            </Response>"""

@app.route('/messages', methods=['GET', 'POST'])
def show_messages():
    api = 'https://api.twilio.com/2010-04-01'
    uri = '/Accounts/' + ACCOUNT_SID + '/Messages.json'
    credentials = (ACCOUNT_SID, AUTH_TOKEN)
    response = requests.get(api + uri, auth=credentials)
    messages = json.loads(response.content)
    pprint(messages)
    return ''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)