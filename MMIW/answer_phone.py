from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Thank you for calling! Missing and Murder indigenous women databate by The A-TEAM, to report a missing person, please say report a missing person.", voice='alice')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
