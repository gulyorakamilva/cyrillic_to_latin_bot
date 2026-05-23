import telebot
from telebot import types
import os 
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	# bot.reply_to(message, "Howdy, how are you doing?")
	keyboard = types.ReplyKeyboardMarkup()
	btn1 = types.KeyboardButton('About me')
	btn2 = types.KeyboardButton('Contact')
	keyboard.add(btn1, btn2)
	bot.send_message(message.chat.id, "Assalomu aleykum", reply_markup=keyboard)
	bot.send_message(message.chat.id, "Assalomu aleykum")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()