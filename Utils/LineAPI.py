from linebot.v3.messaging import ApiClient, MessagingApi, ReplyMessageRequest, Message

def replyM(configuration, replyToken, message: Message):
    with ApiClient(configuration) as apiClient:
        lineBotApi = MessagingApi(apiClient)
        lineBotApi.reply_message_with_http_info(
            ReplyMessageRequest(
                replyToken = replyToken,
                messages = [
                    message
                ]
            )
        )