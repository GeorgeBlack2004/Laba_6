import telebot
import sqlite3
bot = telebot.TeleBot('6980753490:AAFRcWbEFlILnWSz6gkJBWRJOfbl53gKYBI')

@bot.message_handler(content_types=['text'])
def text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")

bot.polling(none_stop=True, interval=0)
