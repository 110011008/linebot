from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('wO2VWea9CKJS/vTq/vm75C8ME7846IfZJC76WvyBODbj5zmU+54W0499rTAKqIoVv+jPzOvj6TRt4rLL4w/33s6ySFK3TZr5EnRqurIJbk4Dyq2dP0SJYNRXFjZpwVkllZfcaHsZJ5Z3zWudWYE33gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c08ecf859fffd7382fd0a1d254cc10cc')


@app.route("/callback", methods=['POST'])
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問什麼?"

    if msg == 'hi':
        r = 'hi'
    elif msg == '吃飽沒'
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = r))


if __name__ == "__main__":
    app.run()