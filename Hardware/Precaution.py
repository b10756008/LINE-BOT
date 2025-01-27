from linebot.v3.messaging import FlexMessage, FlexBubble, FlexBox, FlexText, FlexButton, MessageAction

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

def generateInfoFlexM():
    return FlexMessage(
    type="flex", 
    altText=f"請選擇事項", 
    contents=FlexBubble(
        type="bubble",
        size="kilo",
        body=FlexBox(
            type="box",
            layout="vertical",
            contents=[
                FlexText(type="text", text="想知道何種事項？", weight="bold", size="xl"),
            ]
        ),
        footer=FlexBox(
            type="box",
            layout="vertical",
            contents=generateFlexB(["公告事項", "安全規範"])
        )
    )
)
    
def generateSafeFlexM():
    return FlexMessage(
    type="flex", 
    altText=f"請選擇安全事項", 
    contents=FlexBubble(
        type="bubble",
        size="kilo",
        body=FlexBox(
            type="box",
            layout="vertical",
            contents=[
                FlexText(type="text", text="想知道何種安全事項？", weight="bold", size="xl"),
            ]
        ),
        footer=FlexBox(
            type="box",
            layout="vertical",
            contents=generateFlexB(["行車安全", "工作安全"])
        )
    )
)