import telebot
from telebot import types
import os 
from dotenv import load_dotenv

load_dotenv() 

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	text = "Assalomu aleykum, meni portfolio botimga xush kelibsz."
	keyboard = types.ReplyKeyboardMarkup()
	btn1 = types.KeyboardButton('About me')
	btn2 = types.KeyboardButton('Contact')
	keyboard.add(btn1, btn2)
	bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == "About me":
		bot.send_message(message.chat.id, "men Komilova Gulyora\nMen 16 yoshli talaba bo'lib, dasturlashga qiziqaman. Hozirda Python tilini o'rganmoqdaman.")
	elif message.text == "Contact":
		bot.send_message(message.chat.id, "Bu qism tez orada qo`shiladi.")

bot.infinity_polling()