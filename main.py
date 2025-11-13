# -*- coding: utf-8 -*-
import telebot
import os
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    logger.error("❌ Токен не найден!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "☦️ Бот работает! Исправлена ошибка 409.")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, "Получено: " + message.text)

if __name__ == "__main__":
    print("✅ Бот запущен!")
    while True:
        try:
            bot.remove_webhook()
            time.sleep(1)
            bot.infinity_polling()
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            time.sleep(10)
# Веб-сервер для Render
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🛡️ Бот активен!"

@app.route('/health')
def health():
    return "OK", 200

def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    print("✅ Бот запускается...")
    
    # Запускаем Flask в отдельном потоке
    from threading import Thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Запускаем бота
    while True:
        try:
            bot.remove_webhook()
            time.sleep(1)
            bot.infinity_polling(timeout=60)
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            time.sleep(10)





