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

def generatePlanFlexM():
    return FlexMessage(
    type="flex", 
    altText=f"請選擇指定方案", 
    contents=FlexBubble(
        type="bubble",
        size="kilo",
        body=FlexBox(
            type="box",
            layout="vertical",
            contents=[
                FlexText(type="text", text="想認識何種方案？", weight="bold", size="xl"),
            ]
        ),
        footer=FlexBox(
            type="box",
            layout="vertical",
            contents=generateFlexB(["速在必行", "家速方案"])
        )
    )
)