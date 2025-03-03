from flask import Flask, request
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration, ImageMessage, ImagemapMessage, ImagemapBaseSize, MessageImagemapAction, ImagemapArea, VideoMessage, FlexMessage, FlexBubble, FlexBox, FlexText,FlexImage, URIAction
from linebot.v3.webhooks import MessageEvent, TextMessageContent

from Utils.Config import Config
from Utils.LineAPI import replyM
from Utils.Flex_Template import generateFlexB

import json
import glob
from json import load

app = Flask(__name__)

CONFIG = Config()
configuration = Configuration(
    access_token=CONFIG.accessToken)
handler = WebhookHandler(CONFIG.channelSecret)
configuration2 = Configuration(
    access_token=CONFIG.accessToken2)
handler2 = WebhookHandler(CONFIG.channelSecret2)

def responses_data():
    json_files = glob.glob("responses/*.json")  # 假設 JSON 檔案放在 data 資料夾內
    merged_data = {}
    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            merged_data.update(data)
    return merged_data

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return "Success: Get Callback"

@app.route("/callback2", methods=['POST'])
def callback2():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler2.handle(body, signature)
    return "Success: Get Callback"


@handler.add(MessageEvent, message=TextMessageContent)
def handleTextMessage(event):
    uId = event.source.user_id
    rToken = event.reply_token
    originalM = event.message.text

    data = responses_data()
    # currentUs = uS.get(uId)
    # uS[uId] = UserStatus.SELECT_PRECAUTION
    # 讀取json資料
    key_word = data[originalM]

    # 文字按鈕型
    if key_word['template'] == "flex_button_msg":
        flexM = FlexMessage(
            type="flex", 
            altText=key_word['altText'], 
            contents=FlexBubble(
                type="bubble",
                size="kilo",
                body=FlexBox(
                    type="box",
                    layout="vertical",
                    contents=[
                        FlexText(type="text", text=key_word['contents_text'], weight="bold", size="xl"),
                    ]
                ),
                footer=FlexBox(
                    type="box",
                    layout="vertical",
                    contents=generateFlexB(key_word['footer'])
                )
            )
        )
    # youtube影片型
    elif key_word['template'] == "flex_yt_video":
        flexM = FlexMessage(
            type="flex",
            altText=key_word['altText'],
            contents=FlexBubble(
                type="bubble",
                hero=FlexImage(
                    type="image",
                    url=key_word['video_img_url'],
                    size="full",
                    aspectRatio="16:9",
                    aspectMode="cover",
                    action=URIAction(
                        type="uri",
                        uri=key_word['video_uri']
                    )
                ),
                body=FlexBox(
                    type="box",
                    layout="vertical",
                    contents=[
                        FlexText(type="text", text=f"{key_word['FlexBox']['Main_text']}", weight="bold", size="lg", wrap=True),
                        FlexText(type="text", text=f"{key_word['FlexBox']['Sub_text']}", size="sm", color="#999999", wrap=True)
                    ]
                )
            )
        )
    replyM(configuration, rToken, flexM)



# uS = {}

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
