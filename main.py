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





