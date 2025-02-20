class Config():
    def __init__(self):
        self.accessToken = os.getenv("LINE_ACCESS_TOKEN", "")
        self.channelSecret = os.getenv("LINE_CHANNEL_SECRET", "")

        self.accessToken2 = ""
        self.channelSecret2 = ""
