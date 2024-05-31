import telebot

from settings import*
   
bot = telebot.TeleBot(botId +':'+token)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Your chat ID is: {message.chat.id}")

bot.polling(none_stop=True, interval=10, timeout= 120)