import telebot

from settings import*

# tstArr = []
# for i in range(3):
#     trade_n = {
#     'ticker' : 'KEK',
#     'byPrice': 0,
#     'sellPrice': None,
#     'byTime':None,
#     'sellTime':None,
#     'rsi':i,
# }
#     tstArr.append(trade_n) 
# print(tstArr)

    
bot = telebot.TeleBot(botId +':'+token)

path = 'tBot_MACD_WMA/png/'
file = 'SOLUSDT60.png'


def sendPhoto(path):
    with open( path, 'rb') as f :
        bot.send_photo(myID,f)


def sendMessage(message):
  bot.send_message(myID,message)

# sendMessage('kek')
# @bot.message_handler(content_types=['text'])

# def get_text_messages(message):
#     global tsrArr
#     if message.text == "Список":
#         botReq = '\n'.join(str(el) for el in tstArr)
#         bot.send_message(message.from_user.id, botReq)
#     elif message.text == "Продай 0":
        
#         tstArr[0]['byPrice'] += 25
#         botReq = '\n'.join(str(el) for el in tstArr)
        
#         bot.send_message(message.from_user.id, botReq)
#     else:
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# try :
#     bot.polling(none_stop=True, interval=10, timeout= 120)

# except Exception as ex:
#     print('произошла ошибка')
#     print(str(ex))

def main():
   
   sendMessage('kek')

   pass

if __name__  == "__main__":
   main()