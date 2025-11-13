import telebot
import os
import time
import logging
from flask import Flask
import threading

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    logger.error("❌ Токен не найден!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Веб-сервер для Render
app = Flask(__name__)

@app.route('/')
def home():
    return "🛡️ Бот активен!"

@app.route('/health')
def health():
    return "OK", 200

def run_web_server():
    app.run(host='0.0.0.0', port=10000)

# Телеграм бот
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "☦️ Бот работает!")

if __name__ == "__main__":
    # Запускаем веб-сервер
    web_thread = threading.Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()
    
    print("✅ Бот и веб-сервер запущены")
    
    # Запускаем бота
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            time.sleep(10)

