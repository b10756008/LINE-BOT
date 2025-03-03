import os
class Config():
    def __init__(self):
        self.accessToken = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
        self.channelSecret = os.getenv("LINE_CHANNEL_SECRET")
        # self.accessToken = ""
        # self.channelSecret = ""
    
        self.accessToken2 = ""
        self.channelSecret2 = ""
