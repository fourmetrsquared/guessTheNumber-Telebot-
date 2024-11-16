#!/usr/bin/env python3

import telebot

bot = telebot.TeleBot('API_KEY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat,id, "Hello")


bot.polling(non_stop=True, interval=0)
