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

def generateMediumFlexM():
    return FlexMessage(
    type="flex", 
    altText=f"請選擇傳輸媒介", 
    contents=FlexBubble(
        type="bubble",
        size="kilo",
        body=FlexBox(
            type="box",
            layout="vertical",
            contents=[
                FlexText(type="text", text="想認識何種傳輸媒介？", weight="bold", size="xl"),
            ]
        ),
        footer=FlexBox(
            type="box",
            layout="vertical",
            contents=generateFlexB(["銅線", "光纖"])
        )
    )
)

def generateBrandFlexM(medium):
    if medium == "銅線":
        return FlexMessage(
        type="flex", 
        altText=f"請選擇品牌", 
        contents=FlexBubble(
            type="bubble",
            size="kilo",
            body=FlexBox(
                type="box",
                layout="vertical",
                contents=[
                    FlexText(type="text", text="想認識何種品牌機種？", weight="bold", size="xl"),
                ]
            ),
            footer=FlexBox(
                type="box",
                layout="vertical",
                contents=generateFlexB(["合勤ZyXel", "D-Link"])
            )
        )
    )
    elif medium == "光纖":
        return FlexMessage(
        type="flex", 
        altText=f"請選擇品牌", 
        contents=FlexBubble(
            type="bubble",
            size="kilo",
            body=FlexBox(
                type="box",
                layout="vertical",
                contents=[
                    FlexText(type="text", text="想認識何種品牌機種？", weight="bold", size="xl"),
                ]
            ),
            footer=FlexBox(
                type="box",
                layout="vertical",
                contents=generateFlexB(["Ralink", "Tenda"])
            )
        )
    )

def generateModelFlexM(brand):
    if brand == "合勤ZyXel":
        return FlexMessage(
        type="flex", 
        altText=f"請選擇機種", 
        contents=FlexBubble(
            type="bubble",
            size="kilo",
            body=FlexBox(
                type="box",
                layout="vertical",
                contents=[
                    FlexText(type="text", text="想認識何種機種？", weight="bold", size="xl"),
                ]
            ),
            footer=FlexBox(
                type="box",
                layout="vertical",
                contents=generateFlexB(["P880", "P874", "P883(B)", "6101(ADSL)", "SMC7904W", "T50C"])
            )
        )
    )
    elif brand == "D-Link":
        return FlexMessage(
        type="flex", 
        altText=f"請選擇機種", 
        contents=FlexBubble(
            type="bubble",
            size="kilo",
            body=FlexBox(
                type="box",
                layout="vertical",
                contents=[
                    FlexText(type="text", text="想認識何種機種？", weight="bold", size="xl"),
                ]
            ),
            footer=FlexBox(
                type="box",
                layout="vertical",
                contents=generateFlexB(["6641K", "6740C", "7740C(B)"])
            )
        )
    )