from flask import Flask, request
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration, ImageMessage, ImagemapMessage, ImagemapBaseSize, MessageImagemapAction, ImagemapArea, VideoMessage, FlexMessage, FlexBubble, FlexBox, FlexText,FlexImage, URIAction
from linebot.v3.webhooks import MessageEvent, TextMessageContent

from Hardware import Modem, Plan, Precaution
from Utils.Config import Config
from Utils.Status import UserStatus
from Utils.LineAPI import replyM
      
app = Flask(__name__)

CONFIG = Config()
configuration = Configuration(
    access_token=CONFIG.accessToken)
handler = WebhookHandler(CONFIG.channelSecret)
configuration2 = Configuration(
    access_token=CONFIG.accessToken2)
handler2 = WebhookHandler(CONFIG.channelSecret2)

@app.route("/", methods=["GET"])
def home():
    return "App is running.", 200

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return "Success: Get Callback"

@app.route("/callback2", methods=["POST"])
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

    currentUs = uS.get(uId)
    
    if originalM == ("/注意事項"):
        uS[uId] = UserStatus.SELECT_PRECAUTION
        flexM = Precaution.generateInfoFlexM()
        
        replyM(configuration, rToken, flexM)
    
    elif currentUs == UserStatus.SELECT_PRECAUTION:
        if originalM == "安全規範":
            uS[uId] = UserStatus.SELECT_PRECAUTION_INFO
            
            flexM = Precaution.generateSafeFlexM()
        
            replyM(configuration, rToken, flexM)
    
    elif currentUs == UserStatus.SELECT_PRECAUTION_INFO:
        del uS[uId]
        flexM = FlexMessage(
            type="flex",
            altText="播放影片",
            contents=FlexBubble(
                type="bubble",
                hero=FlexImage(
                    type="image",
                    url="https://img.youtube.com/vi/OKA1kO1VKnI/maxresdefault.jpg",
                    size="full",
                    aspectRatio="16:9",
                    aspectMode="cover",
                    action=URIAction(
                        type="uri",
                        uri="https://www.youtube.com/watch?v=OKA1kO1VKnI"
                    )
                ),
                body=FlexBox(
                    type="box",
                    layout="vertical",
                    contents=[
                        FlexText(type="text", text="行車安全宣導", weight="bold", size="lg", wrap=True),
                        FlexText(type="text", text="請點擊上方縮圖播放影片。", size="sm", color="#999999", wrap=True)
                    ]
                )
            )
        )

        replyM(configuration, rToken, flexM)

    elif originalM == ("/認識硬體"):
        uS[uId] = UserStatus.SELECT_DEVICE
        imagemapMessage = ImagemapMessage(
            type="imagemap",
            baseUrl="https://raw.githubusercontent.com/b10756008/LINE-BOT/refs/heads/main/img/richmessage_003_test.png?token=GHSAT0AAAAAAC56ONGLIHVJULKZJRJVIXN2Z4XVIAA",
            altText="硬體設備選單",
            baseSize=ImagemapBaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text="數據機",
                    area=ImagemapArea(x=0, y=0, height=540, width=540)
                ),
                MessageImagemapAction(
                    text="分享器",
                    area=ImagemapArea(x=540, y=0, height=540, width=540)
                ),
                MessageImagemapAction(
                    text="STB",
                    area=ImagemapArea(x=0, y=540, height=540, width=540)
                ),
                MessageImagemapAction(
                    text="專業設備",
                    area=ImagemapArea(x=540, y=540, height=540, width=540)
                ),
            ]
        )

        replyM(configuration, rToken, imagemapMessage)
        
    elif currentUs == UserStatus.SELECT_DEVICE:
        if originalM == "數據機":
            uS[uId] = UserStatus.SELECT_MODEM_MEDIUM
            flexM = Modem.generateMediumFlexM()
            replyM(configuration, rToken, flexM)

    elif currentUs == UserStatus.SELECT_MODEM_MEDIUM:
        uS[uId] = UserStatus.SELECT_MODEM_BRAND
        flexM = Modem.generateBrandFlexM(originalM)
        replyM(configuration, rToken, flexM)

    elif currentUs == UserStatus.SELECT_MODEM_BRAND:
        uS[uId] = UserStatus.SELECT_MODEM_MODEL
        flexM = Modem.generateModelFlexM(originalM)
        replyM(configuration, rToken, flexM)

    elif currentUs == UserStatus.SELECT_MODEM_MODEL:
        if originalM == "P880":
            del uS[uId]
            replyM(configuration, rToken, ImageMessage(
                type="image",
                original_content_url="",
                previewImageUrl=""
            ))
            
@handler2.add(MessageEvent, message=TextMessageContent)
def handleTextMessage2(event):
    uId = event.source.user_id
    replyT = event.reply_token
    originalM = event.message.text
    currentUs = uS2.get(uId)
    
    if originalM == ("/最新方案"):
        uS2[uId] = UserStatus.SELECT_PLAN
        flexM = Plan.generatePlanFlexM()
        replyM(configuration2, replyT, flexM)
        
    elif currentUs == UserStatus.SELECT_PLAN:
        if originalM == "速在必行":
            del uS2[uId]
            replyM(configuration2, replyT, ImageMessage(
                type="image",
                original_content_url="",
                previewImageUrl=""
            ))
        elif originalM == "家速方案":
            del uS2[uId]
            replyM(configuration2, replyT, ImageMessage(
                type="image",
                original_content_url="",
                previewImageUrl=""
            ))

uS = {}
uS2 = {}

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
