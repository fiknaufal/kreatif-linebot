import os
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
from linebot.models.send_messages import ImageSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('HTAFMVup4+eKBJp5ndZz+xrlCutjVVH5ZRBjyjTCCT0LxJU8SIbW4XPVwLOQ2TzsC+WGdlyHYbsLIJRGW8QlSebK13zvlKJoJutHLf+630bNTVmMD1lT9+mYHcweUBtqBqvq2iTT/euskK/rXUd7JgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2d18e5f4abccfd57cfff0aff9ceeadc2')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """
    image_message = ImageSendMessage(
    original_content_url='https://drive.google.com/file/d/1GFDObqx3WLx5ul7fprHRnxt_rG9UJPSy/view',
    preview_image_url='https://drive.google.com/file/d/1jMzWzfLD9MjBZR0UCiywCY97mGq-Z_W6/view'
    )
    if event.message.text == "bot, ultah hari ini" :
        line_bot_api.reply_message(event.reply_token, image_message)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
