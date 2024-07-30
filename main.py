from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7354061639:AAHhRpJsx-vIMbF79ujg-f73i8o9epK2Ga0'
WEBHOOK_URL = f"https://your-vercel-app.vercel.app/{TELEGRAM_BOT_TOKEN}"

@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        message_text = data["message"]["text"]

        if message_text == "/start":
            tg_web_app_data = request.json.get('message').get('web_app_data').get('data')
            send_message(chat_id, f"tgWebAppData: {tg_web_app_data}")
    
    return '', 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
