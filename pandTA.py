from  getData import getKline
import pandas as pd
import pandas_ta as ta
# import matplotlib.pyplot as plt
symb = 'SOLUSDT'
tf='60'
limit=100


def getIndicators(df,sett):
    df['rsi'] = ta.rsi(close=df.Close, length=14)
    df['wma'] = ta.wma(close=df.Close, length=int(sett['WMA']))
    df['atr'] = ta.atr(df.High,df.Low,df.Close, length= 5)
    lol = ta.macd(close=df.Close,fast=12,slow=26,signal=9)  #  pd.DataFrame: macd, histogram, signal columns.
    lol.rename(columns = {'MACD_12_26_9':'macd', 'MACDh_12_26_9':'hist', 'MACDs_12_26_9':'sig'}, inplace = True )
    df = df.join(lol)
    return df

# print(help(ta.macd))
def main():
    df = getKline(symb,tf,limit)
    print(getIndicators(df))

if __name__ == '__main__':
    main()
    pass