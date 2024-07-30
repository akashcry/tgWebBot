from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7354061639:AAHhRpJsx-vIMbF79ujg-f73i8o9epK2Ga0'

@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.json

    if not data:
        return jsonify({'error': 'No JSON data received'}), 400

    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        message_text = message.get("text", "")

        if message_text == "/start":
            send_message(chat_id, "Welcome to the bot! Click the button below to open the web app.")
            send_web_app_button(chat_id)

    if "callback_query" in data:
        chat_id = data["callback_query"]["message"]["chat"]["id"]
        tg_web_app_data = data["callback_query"]["data"]
        send_message(chat_id, f"tgWebAppData: {tg_web_app_data}")

    return '', 200

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

def send_web_app_button(chat_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "Open Web App",
        "reply_markup": {
            "inline_keyboard": [[{
                "text": "Open Web App",
                "web_app": {"url": "https://your-vercel-url.vercel.app"}
            }]]
        }
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=True)
