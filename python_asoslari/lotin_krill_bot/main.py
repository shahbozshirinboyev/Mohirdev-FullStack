"""
01.05.2025
MohirDev.Uz da FullStack Dasturlash
Lotin - Krill BOT
Dasturchi: Shahboz Shirinboyev
"""
from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7144085404:AAHw_hG_Pfq8WQGDtsZARu65lmIOUthYgUo'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  javob = "Assalomu alaykum, Xush kelibsiz!"
  javob += "\nMatn kiriting:"
  bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  msg = message.text
  javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
  # if msg.isascii():
  #   javob = to_cyrillic(msg)
  # else:
  #   javob = to_latin(msg)
  bot.reply_to(message, javob(msg))

bot.infinity_polling()



# matn = input("Matn kiriting: ")
# if matn.isascii():
#   print(to_cyrillic(matn))
# else:
#   print(to_latin(matn))