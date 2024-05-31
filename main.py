# from settings import tradeListName , settingsName
from settings import*
from bot import bot
from getData import getKline
from helpers import readJson , writeJson
from check import check
from plot import makePlot
import logging
import time
import threading



tickerList=[]

def main():
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
    # time.sleep(5)
    global settingsList, tickerList
    settingsList = readJson(settingsName)
    Limit = settingsList['limit']
    interval = settingsList['period']
    percent = settingsList['percent']
    resp = settingsList['resp']
    print('kek')

    try:
        # def flow():

        with open(tradeListName) as f:
            rawlist = f.read()
        tickerList = list(rawlist.split(","))
        print('restart with new settings', type(tickerList))
        # lol=10
        # try:

        while True:

            for symbol in tickerList:

                print(symbol,len(tickerList))
                kLineDf = getKline(symbol, interval, Limit)
                
                event = check(kLineDf,float(percent))
                orderTime = kLineDf['Date'].iloc[-1]
                # print(orderTime)
                if event:
                    try: 

                        makePlot(symbol, kLineDf,  settingsList )
                        # sendMessage(myID,symbol)
                    except Exception as e:
                        logging.error('sendMessage: ',exc_info=True)

                    # добавили в бан лист
                    tempBan = readJson(banListName)
                    tempBan.append({'symbol': symbol,
                                    'timeOfBan': str(orderTime),
                                    'timeRespawn': str(orderTime + sleepTime * int(resp))

                                    })
                    writeJson(banListName, tempBan)

                    # удалили из текущего торгового листа
                    tickerList.remove(symbol)
                    with open(tradeListName, 'w') as output:
                        output.write(','.join(tickerList))


                # tab = getIndicators(kLineDf, settingsList)
                time.sleep(1)
        
    except Exception as e:
        logging.error(symbol,exc_info=True)
        time.sleep(30)
        main()


def respawn():
    while True:
        global tickerList
        tempBanList = readJson(banListName)
        nowTime = int(time.time())
        print ('chek respawn', len(tempBanList))
        if len(tempBanList) > 0:
            for item in tempBanList:
                # print(item)
                if int(item['timeRespawn'] )< nowTime:
                    tickerList.append(item['symbol'])
                    with open(tradeListName, 'w') as output:
                        output.write(','.join(tickerList))
                    tempBanList.remove(item)
                    writeJson(banListName, tempBanList)

        time.sleep(600)

@bot.message_handler(commands=['int'])
def set_int(message):
    tempJS = readJson(settingsName)
    print(tempJS,type(tempJS))
    try:
        data = message.text.split('/int ', 1)[1]
        tempJS['period'] = str(data)
        writeJson(settingsName,tempJS)
        
        bot.reply_to(message, f"обновлен интервал '{data}' ")
    except IndexError:
        bot.reply_to(message, "ошибка изменения попробуй еще")



@bot.message_handler(commands=['start'])
def check_settings(message):
    setArr = ['/list пришлет список монет', 
              '/lim 300 установит кол-во запрвшиваемых свечей',
              '/int 60 установит интервал 60',
              '/per 2.2 множитель увеличения объемов ',
               '/resp 60 установит время нахождения в бане в минутах',
               '/add BTCUSDT добавит в торговый лист',
               '/dell BTCUSDT удалит из торгового листа'
              
               ]
    try:
        botReq = '\n'.join(str(el) for el in setArr)
        bot.send_message(message.from_user.id, botReq)
    except IndexError:
        bot.reply_to(message, "что то пошло не так")

@bot.message_handler(commands=['per'])
def set_per(message):
    tempJS = readJson(settingsName)
    print(tempJS,type(tempJS))
    try:
        data = message.text.split('/per ', 1)[1]
        tempJS['percent'] = str(data)
        writeJson(settingsName,tempJS)
        
        bot.reply_to(message, f"обновлен процент '{data}' ")
    except IndexError:
        bot.reply_to(message, "ошибка изменения попробуй еще")

@bot.message_handler(commands=['lim'])
def set_lim(message):
    tempJS = readJson(settingsName)
    print(tempJS,type(tempJS))
    try:
        data = message.text.split('/per ', 1)[1]
        tempJS['limit'] = str(data)
        writeJson(settingsName,tempJS)
        
        bot.reply_to(message, f"обновлен лимит '{data}' ")
    except IndexError:
        bot.reply_to(message, "ошибка изменения попробуй еще")

@bot.message_handler(commands=['resp'])
def set_resp(message):
    tempJS = readJson(settingsName)
    print(tempJS,type(tempJS))
    try:
        data = message.text.split('/resp ', 1)[1]
        tempJS['resp'] = str(data)
        writeJson(settingsName,tempJS)
        
        bot.reply_to(message, f"обновлено время ожидания'{data}' ")
    except IndexError:
        bot.reply_to(message, "ошибка изменения попробуй еще")


@bot.message_handler(commands=['list'])
def get_text_messages(message):
    global settingsList
    with open(tradeListName) as f:
        rawlist = f.read()
    if rawlist:
        temp = list(rawlist.split(","))
        print(temp)
        botReq = '\n'.join(str(el) for el in temp)
        bot.send_message(message.from_user.id, botReq)
    
    
    

@bot.message_handler(commands=['add'])
def add_name(message):
    global tickerList
    try:
        name = message.text.split('/add ', 1)[1]
        # with open(tradeListName) as f:
        #     rawlist = f.read()
        # tickerList = list(rawlist.split(","))

        tickerList.append(name)
        with open(tradeListName, 'w') as output:
            output.write(','.join(tickerList))

        bot.reply_to(message, f" '{name}' добавлен в список")
    except IndexError:
        bot.reply_to(message, "ошибка добавления попробуй еще")

@bot.message_handler(commands=['dell'])
def add_name(message):
    global tickerList
    try:
        name = message.text.split('/dell ', 1)[1]
        # with open(tradeListName) as f:
        #     rawlist = f.read()
        # tickerList = list(rawlist.split(","))

        rm_index = tickerList.index(name)
        tickerList.pop(rm_index)

        with open(tradeListName, 'w') as output:
            output.write(','.join(tickerList))
        bot.reply_to(message, f" '{name}' удален из списка")
    except IndexError:
        bot.reply_to(message, "ошибка добавления попробуй еще")


def start_bot():
    try:
        bot.polling(none_stop=True, interval=10, timeout= 120)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(15)  # Ждем перед перезапуском



if __name__ == '__main__':

    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    th1 = threading.Thread(target=respawn, daemon=True)
    th1.start()
    
    main()
 