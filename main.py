import telebot
import os
import time
import logging
from flask import Flask
from threading import Thread

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    logger.error("❌ Токен не найден!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Веб-сервер
app = Flask(__name__)

@app.route('/')
def home():
    return "🛡️ Бот активен!"

@app.route('/health')
def health():
    return "OK", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "✅ Бот работает!")

if __name__ == "__main__":
    # Останавливаем старые соединения
    try:
        bot.remove_webhook()
        time.sleep(2)
    except:
        pass
    
    # Запускаем Flask
    def run_flask():
        app.run(host='0.0.0.0', port=10000)
    
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    print("🚀 Запуск бота...")
    
    # Запускаем бота
    while True:
        try:
            bot.infinity_polling(timeout=30, long_polling_timeout=30)
        except Exception as e:
            logger.error(f"❌ Ошибка: {e}")
            time.sleep(30)
