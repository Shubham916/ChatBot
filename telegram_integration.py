from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from model_training import predict_intent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve token from environment variables
telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your chatbot.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    intent = predict_intent(user_input)
    update.message.reply_text(f'Intent: {intent}')

updater = Updater(telegram_bot_token)

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
