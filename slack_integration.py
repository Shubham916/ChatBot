from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from model_training import predict_intent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve token and secret from environment variables
slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
slack_signing_secret = os.environ.get('SLACK_SIGNING_SECRET')

slack_app = App(token=slack_bot_token, signing_secret=slack_signing_secret)
handler = SlackRequestHandler(slack_app)

@slack_app.event("message")
def handle_message_events(body, say):
    text = body['event']['text']
    intent = predict_intent(text)
    say(f'Intent: {intent}')

flask_app = Flask(__name__)

@flask_app.route('/slack/events', methods=['POST'])
def slack_events():
    return handler.handle(request)

if __name__ == '__main__':
    flask_app.run(port=3000)
