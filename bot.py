"""Библиотеки"""
import telebot
""""""

"""Переменные"""
bot = telebot.TeleBot('1039780601:AAGxjBKfAa9q8Tloc-_C0wIfRErqbUQmCws')
""""""

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()