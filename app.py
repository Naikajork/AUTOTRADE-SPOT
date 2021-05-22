from flask import Flask, request
import json

from BinanceTrade.Trade import ReceiveSignals
from Line.notify import SendMsg

app = Flask(__name__)

@app.route("/SIGNALS", methods = ['POST'])
def SIGNALS_RECEIVER():
    if request.method == "POST":
        msg = request.data.decode("utf-8")
        json_msg = json.loads(msg)
        print(json_msg)

        msg = ReceiveSignals(signal_data_dict = json_msg)
        SendMsg(msg = msg)

    return "200"

from Line.LineBot import handler

@app.route("/linebot", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run(debug=True, port=8080)