from getData import getKline

interval = '15'
symbol = 'SOLUSDT'
limit = 500


def check(df,percent):
    volume  = df['Volume']
    if volume.iloc[-1] > volume.iloc[-2]*percent:
        return True
    else:
        return False
    pass


if __name__ == '__main__':


    kek = check(getKline(symbol,'15','200'),1.3)
    print(kek)