# -*- coding: utf-8 -*-

# Напишите код программы на Python, которая будет в реальном времени (с максимально возможной скоростью)
# считывать текущую цену фьючерса XRP/USDT на бирже Binance.
# В случае, если цена упала на 1% от максимальной цены за последний час, программа должна вывести сообщение
# в консоль.
# При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.

from ws_client import WsClient as bnb_client
from tracker import Tracker as tracker

while True:
    symbol = input('Input desirable symbol to track: ').replace('/', '').lower()

    # Let's do little check about if symbol ends right
    # (also we could check if the base coin is in our allowed to trade list)
    if symbol.endswith('usdt') or symbol.endswith('busd'):
        break
    else:
        print(f'Input correct symbol ending with USDT or BUSD.')

lookback = 60 # quantity of minutes for looking back to define max price

if __name__ == '__main__':
    client = bnb_client(symbol)
    tr = tracker(symbol, lookback)
    tr.GetPriceMax()
    while True:
        if client.IsConnected():
            tr.UpdateMax(client.GetPriceLast())