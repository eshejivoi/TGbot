from config import token

import random

import telebot

bot = telebot.TeleBot(token)

sap_list = ['без ошибок не бывает успеха', 'не сдавайся', 'будь настойчив', 'всем нужно отдыхать']

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['pic'])
def send_pic(message):
    send = bot.send_message(message.from_user.id, 'отправь свою картинку...')
    bot.register_next_step_handler(send, get_user_pics)
    return

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """этот бот находиться в разработке, будьте терпеливы если хотите получить больше инфомации""")

@bot.message_handler(commands=['sap'])
def messagelist(message):
  bot.reply_to(message, """я могу оказать тебе поддержку""")
  bot.send_message(message.chat.id, random.choice(sap_list))

#@bot.message_handler(commands=['car'])
#class Car:
#    def __init__(self, year = "2022", color = "красный", car_brand = "Mercedes-Benz A-Класс AMG W177"):
#        self.year = year
#        self.color = color
#        self.car_brand = car_brand
#
#
#    def info(self):
#        bot.send_message("Год машины ", self.year)
#        bot.send_message("Цвет ", self.color)
#        bot.send_message("Бренд машины ", self.car_brand)
#
#car = Car()
#Car().info()

@bot.message_handler(content_types=['photo'])
def get_user_pics(message):
    send = bot.send_message(message.from_user.id, "классное фото!")
    bot.register_next_step_handler(send, get_user_pics)
    return



bot.polling()