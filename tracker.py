# -*- coding: utf-8 -*-
import requests

class Tracker:
    def __init__(self, symbol, lookback):
        self.symbol = symbol.upper()
        self.interval = '1m'
        self.lookback = lookback
        self.url = f'https://data.binance.com/api/v3/klines?symbol={self.symbol}&interval={self.interval}&limit={self.lookback}'
        self.price_max = -1.0

    def GetPriceMax(self):
        try:
            candles = requests.get(self.url).json()
            # print(candles)
            high = []
            for candle in candles:
                high.append(float(candle[2]))
            # print(high)
            self.price_max = max(high)
            # self.price_max = high[-1] # i used last price for max update comparison to get faster debug
        except Exception as e:
            print(f'Tracker.GetPriceMax exceptions:\n{e}')

    def UpdateMax(self, price_new):
        if 0 < self.price_max < price_new:
            print(f'We got new high = {price_new}, previous high = {self.price_max}')
            self.price_max = price_new


