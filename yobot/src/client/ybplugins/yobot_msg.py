from urllib.parse import urljoin


class Message:
    Passive = True
    Active = False
    Request = False

    def __init__(self, glo_setting: dict, *args, **kwargs):
        self.version = glo_setting["verinfo"]["ver_name"]
        self.setting = glo_setting
        self.help_page = urljoin(
            glo_setting["public_address"],
            '{}help/'.format(glo_setting['public_basepath']))
        self.help_yobot =  urljoin(
            glo_setting["public_address"],
            '{}helpOfYobot/'.format(glo_setting['public_basepath']))
        self.help_hoshino =  urljoin(
            glo_setting["public_address"],
            '{}helpOfHoshino/'.format(glo_setting['public_basepath']))
        if glo_setting['web_mode_hint']:
            self.help_page += '\n\n如果无法打开，请仔细阅读教程中《链接无法打开》的说明'

    @staticmethod
    def match(cmd: str) -> int:
        if cmd == "ver" or cmd == "V" or cmd == "version":
            return 99
        elif cmd == "帮助" or cmd == "help":
            return 98
        elif cmd == "手册":
            return 97
        else:
            return 0

    def execute(self, match_num: int, msg: dict) -> dict:
        if match_num == 99:
            reply = self.version
        elif match_num == 98:
            reply = """
发送以下关键词查看更多：
[帮助pcr会战]
[帮助pcr查询]
[帮助pcr娱乐]
[帮助pcr订阅]
[帮助kancolle]
[帮助通用]""".strip() + "\n以下可从网页查看更多详情：\npcr会战帮助：" + self.help_yobot + "\ngithub仓库：https://github.com/9cats/pcrbot"
        elif match_num == 97:
            reply = urljoin(
                self.setting["public_address"],
                '{}manual/'.format(self.setting['public_basepath']))
        elif match_num == 2:
            reply = "boss被击败后我会提醒下树"
        else:
            reply = "此功能已经不再可用，请查看"+self.help_page
        return {
            "reply": reply,
            "block": True
        }
