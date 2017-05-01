from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/call", methods=['GET', 'POST'])
def gate_please():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Play digits="wwww9999"></Play>
    </Response>"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
