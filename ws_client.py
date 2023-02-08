# -*- coding: utf-8 -*-

import threading, websocket, json

class WsClient:
    def __init__(self, symbol):
        self.symbol = symbol
        self.url = f'wss://stream.binance.com:9443/ws/{self.symbol}@ticker'
        self.price_last = 0.0
        self.is_connected = False
        self.ws = self.GetWs()
        self.task = threading.Thread(target=self.ws.run_forever)
        self.task.start()

    def OnOpen(self, ws):
        print(f"{self.symbol}: ws connection is opened")

    def OnMessage(self, ws, message):
        try:
            # print("Received a message BINANCE")
            # print(f'Message: {message}')
            self.price_last = float(json.loads(message)['c'])
            self.is_connected = True
            # print(f'close price = {self.price_last}')
        except Exception as e:
            print(f'WS {self.symbol} exception: {e}')

    def OnClose(self, ws):
        print(f'WS connection {self.symbol} is closing...')
        pass

    # Establishing WS connection
    def GetWs(self):
        try:
            ws = websocket.WebSocketApp(self.url, on_open=self.OnOpen, on_message=self.OnMessage, on_close=self.OnClose)
            return ws
        except Exception as e:
            print(f"GetWS exception:\n{e}")
            return

    # Return last known price
    def GetPriceLast(self):
        return self.price_last

    # Flag that ws is opened successfully and we got at least one msg (updated last price)
    def IsConnected(self):
        return self.is_connected

