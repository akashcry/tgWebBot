import logging

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
TELEGRAM_BOT_TOKEN = '7354061639:AAHhRpJsx-vIMbF79ujg-f73i8o9epK2Ga0'
@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.json

    if data is None:
        app.logger.error("Received request with no JSON data.")
        return jsonify({'error': 'No JSON data received'}), 400

    app.logger.debug('Received data: %s', data)

    message = data.get("message")
    if not message:
        app.logger.error("No message found in the request data.")
        return jsonify({'error': 'No message found'}), 400

    chat = message.get("chat")
    if not chat:
        app.logger.error("No chat information found in the message.")
        return jsonify({'error': 'No chat information found'}), 400

    chat_id = chat.get("id")
    if not chat_id:
        app.logger.error("No chat ID found in the chat information.")
        return jsonify({'error': 'No chat ID found'}), 400

    message_text = message.get("text", "")
    app.logger.debug('Chat ID: %s, Message Text: %s', chat_id, message_text)

    if message_text == "/start":
        web_app_data = message.get("web_app_data", {})
        tg_web_app_data = web_app_data.get("data", "No tg-web-app-data found")
        app.logger.debug('tgWebAppData: %s', tg_web_app_data)
        send_message(chat_id, f"tgWebAppData: {tg_web_app_data}")
    
    return '', 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    app.logger.debug('Send message response: %s', response.json())

if __name__ == "__main__":
    app.run()
