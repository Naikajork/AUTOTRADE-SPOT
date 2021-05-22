from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

try:
    from config_dev import *
except:
    from config_prod import *

from DB.Firebasedb import UpdateBotSetting

line_bot_api = LineBotApi(LINE_BOT_ACCESS_TOKEN)
handler = WebhookHandler(LINE_BOT_CHANNEL_SECRET)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message_from_user = event.message.text

    if message_from_user == "/stop":
        try:
            UpdateBotSetting(key="RUN",value=False)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="การเปลี่ยนแปลงเสร็จสิ้น"))

        except Exception as e:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="เกิดข้อผิดพลาด {}".format(e)))

    elif message_from_user == "/start":
        try:
            UpdateBotSetting(key="RUN",value=True)

            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="การเปลี่ยนแปลงเสร็จสิ้น"))

        except Exception as e:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="เกิดข้อผิดพลาด {}".format(e)))


