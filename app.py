from flask import Flask, request
import json
from binance.spot import Spot as Client


app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():

    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        quantity = data['quantity']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']

        
        params = {
            "symbol": ticker,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "isIsolated": "TRUE",
            "sideEffectType": "MARGIN_BUY",
        }
        
        params2 = {
            "symbol": ticker,
            "side": side,
            "type": "MARKET",
            "quantity": quantity,
            "isIsolated": "TRUE",
            "sideEffectType": "AUTO_REPAY",
        }

        if side == "BUY":
            Client(binanceApiKey, binanceSecretKey).new_margin_order(**params2)
        if side == "SELL":
            Client(binanceApiKey, binanceSecretKey).new_margin_order(**params)

    except:
        pass
    return {
        "code": "success",
    }










