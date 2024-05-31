# from settings import tradeListName , settingsName
from settings import*
from bot import sendMessage
from getData import getKline
from helpers import readJson
from check import check
import logging
import time



def main():
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")
    # time.sleep(5)
    global settingsList, tickerList
    settingsList = readJson(settingsName)
    Limit = settingsList['limit']
    interval = settingsList['period']
    percent = settingsList['percent']
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
                print(kLineDf)
                event = check(kLineDf,float(percent))
                if event:
                    try: 

                        
                        sendMessage(myID,symbol)
                    except Exception as e:
                        logging.error('sendMessage: ',exc_info=True)


                # tab = getIndicators(kLineDf, settingsList)
                time.sleep(1)
        
    except Exception as e:
        logging.error('main: ',exc_info=True)
        time.sleep(5)
        main()


    pass

if __name__ == '__main__':
    main()