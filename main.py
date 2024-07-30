from flask import Flask, request
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

app = Flask(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dp.process_update(update)
    return "ok", 200

def start(update, context):
    update.message.reply_text("Send me some Web App Data!")

def handle_message(update, context):
    tg_web_app_data = update.message.text
    update.message.reply_text(f"Received Web App Data: {tg_web_app_data}")

dp = Dispatcher(bot, None, use_context=True)
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
