from config import config
from config.setting import Setting
from tools.tool import ToolUtil


class BaseRes(object):
    def __init__(self, data, isParseRes) -> None:
        super().__init__()
        self.raw = data
        self.data = {}
        self.code = 0
        self.message = ""
        self.reqBak = None
        self.isParseRes = isParseRes
        if isParseRes:
            ToolUtil.ParseFromData(self, self.raw.text)

    def __str__(self):
        if Setting.LogIndex.value == 0:
            return ""
        elif Setting.LogIndex.value == 1:
            return "code:{}".format(self.code)

        if self.isParseRes:
            data = self.GetText()
        else:
            data = ""
        return "code:{}, raw:{}".format(self.code, data.replace("\n", ""))

    def GetText(self):
        if hasattr(self.raw, "text"):
            return self.raw.text
        return ""
