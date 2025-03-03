from linebot.v3.messaging import FlexMessage, FlexBubble, FlexBox, FlexText, FlexButton, MessageAction
# flex_msg的button
def generateFlexB(items: list):
    result = []
    for itme in items:
        result.append(FlexButton(
            type="button",
            style="link",
            height="sm",
            action=MessageAction(
                type="message",
                label=itme,
                text=itme
            )
        ))
    return result