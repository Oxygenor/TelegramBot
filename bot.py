"""Библиотеки"""
import telebot
""""""

"""Переменные"""
bot = telebot.TeleBot('')
""""""

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()