import pandas as pd
import mplfinance as mpf
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from bot import sendPhoto
from settings import*
buffer = BytesIO()
symbol = 'BTCUSDT'
folder = 'tBot_MACD_WMA/png/'


myStyle = {
    "base_mpl_style": "dark_background",
    "marketcolors": {
        "candle": {"up": "#3dc985", "down": "#ef4f60"},  
        "edge": {"up": "#3dc985", "down": "#ef4f60"},  
        "wick": {"up": "#3dc985", "down": "#ef4f60"},  
        "ohlc": {"up": "green", "down": "red"},
        "volume": {"up": "#247252", "down": "#82333f"},  
        "vcedge": {"up": "green", "down": "red"},  
        "vcdopcod": False,
        "alpha": 1,
    },
    "mavcolors": ("#ad7739", "#a63ab2", "#62b8ba"),
    "facecolor": "#1b1f24",
    "gridcolor": "#2c2e31",
    "gridstyle": "--",
    "y_on_right": True,
    "rc": {
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.edgecolor": "#474d56",
        "axes.titlecolor": "red",
        "figure.facecolor": "#161a1e",
        "figure.titlesize": "x-large",
        "figure.titleweight": "semibold",
    },
    "base_mpf_style": "binance-dark",
}

# # add your own style by passing in kwargs    
# s = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size': 6})
# fig = mpf.figure(figsize=(10, 7), style=s) # pass in the self defined style to the whole canvas
# ax = fig.add_subplot(2,1,1) # main candle stick chart subplot, you can also pass in the self defined style here only for this subplot
# av = fig.add_subplot(2,1,2, sharex=ax)  # volume chart subplot
# mpf.plot(price_data, type='candle', ax=ax, volume=av)

# def makePlot(Klines,  timeFrame , symb , wma ,macd, signal, hist ,atr,line0,fractSupp):#  by, sell):
def makePlot(symb, df,  settings ):
    # df['Date'] = df['Date'].astype(np.int64)
    # df['Date'] = pd.to_datetime(df['Date'], unit = 'ms')
    df['Date'] = pd.to_datetime(df['Date'], unit= 's')
    print(df['Date'])
    df = df.set_index('Date')


    Limit = settings['limit']
    interval = settings['period']
    percent = settings['percent']

    addplot  =  [
        # mpf.make_addplot(wma , color="orange", width=1),
    #              mpf.make_addplot(Talib[ "middle_band"] , color="dodgerblue", width=1),
                #  mpf.make_addplot(hist,type='bar',panel=1,secondary_y=False),
                # mpf.make_addplot(macd,panel=1,color='blue',secondary_y=False, width=1),
                # mpf.make_addplot(signal,panel=1,color='orange',secondary_y=False, width=1),
                # mpf.make_addplot(atr,panel=1,color='black',secondary_y=False, width=1),
                # mpf.make_addplot(by, scatter=True , color='blue', marker='^', ),
                # mpf.make_addplot(sell, scatter=True , color='blue', marker='v' ),
                # mpf.make_addplot(line0,panel='lower',color='g',secondary_y=False),
                # mpf.make_addplot(fractSupp, scatter=True , color='green', ),
                # mpf.make_addplot(fractRes, scatter=True , color='red', ),                
                
    ]
    

    
    mpf.plot(df,
            type='candle',
            # addplot = addplot,
            # hlines=dict(hlines=levels, linewidths = 0.2),
            style=myStyle,
            title=symb + ' ' + str(interval)  ,
            ylabel='USDT',
            figratio=(9,5),
            savefig= 'temp.png',
            volume=True,
             )  
    sendPhoto('temp.png')


    # mpf.show()
            

if __name__ == '__main__':
    
    
    from getData import getKline
    from helpers import readJson
    settings = readJson(settingsName)
    Limit = settings['limit']
    interval = settings['period']
    percent = settings['percent']
    df = getKline(symbol, interval, Limit)
    png = makePlot(symbol,df,settings)

    pass