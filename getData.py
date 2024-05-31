import pandas as pd
from pybit.unified_trading import HTTP

import numpy as np
import time
import requests

interval = '15'
symbol = 'SOLUSDT'
limit = 500
category = 'linear'

session = HTTP(
     testnet=False,

    max_retries=3,
    retry_delay=30,
)

def getKline(symb, timeFrame, limit ,start = False, end = False):  #limit):
    rawReq = session.get_kline(
        category=category,
        symbol=symb,
        interval=timeFrame,
        start = start,
        end = end,
        limit = limit
    )
    req = rawReq ['result'] ['list']
    req.reverse()
    dataFrame = pd.DataFrame(req)
    # jReq = rawReq.json()
    # pdReq = pd.DataFrame(jReq, ['result']) 
    
    cleanDf = pd.DataFrame()
    cleanDf['Date'] = dataFrame.iloc[:,0].apply(lambda x: x[0:-3]) #.astype(np.int64)/1000
    cleanDf['Date'] = cleanDf['Date'].astype(np.int64)
    # cleanDf['Date'] = round(cleanDf['Date'])
    # cleanDf['Date'] = pd.to_datetime(cleanDf['Date'], unit = 'us') #  , unit = 'ns'
    # когда не трогаю отдает 17106.80400.000 (ms)
    # а нужно # когда не трогаю отдает 1709074800 (us)(10 знаков)
    cleanDf['Open'] = dataFrame.iloc[:,1].astype(float)
    cleanDf['High'] = dataFrame.iloc[:,2].astype(float)
    cleanDf['Low'] = dataFrame.iloc[:,3].astype(float)
    cleanDf['Close'] = dataFrame.iloc[:,4].astype(float)
    cleanDf['Volume'] = dataFrame.iloc[:,5].astype(float)
    # cleanDf = cleanDf.set_index('Date')
    # print(cleanDf)
    return cleanDf

# tst = getKline(symb,timeFrame,limit)
# print(tst)


def main ():
    data  = getKline(symbol, interval , limit)
    print(data)
    pass
    
if __name__ == '__main__':
    main()