from flask import Flask, request, abort

import requests

import random

from bs4 import BeautifulSoup

from app import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Channel access token')
handler = WebhookHandler('Channel secret')

@app.route("/")
def test():
    return"OK"

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
    word=event.message.text
    url=f'https://www.google.com/search?q={word}&source=lnms&tbm=isch'
    response=requests.get(url)
    soup= BeautifulSoup(response.text)
    images=soup.find_all('img')
    del images[0]
    image_url=random.choice(images)['src']
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
        original_content_url= image_url,
        preview_image_url=image_url))


if __name__ == "__main__":
    app.run()