import telebot

from settings import*


    
bot = telebot.TeleBot(botId +':'+token)

path = 'tBot_MACD_WMA/png/'
file = 'SOLUSDT60.png'


def sendPhoto(path):
    with open( path, 'rb') as f :
        bot.send_photo(myID,f)


def sendMessage(message):
  bot.send_message(myID,message)

def main():
   
   sendMessage('kek')

   pass

if __name__  == "__main__":
   main()