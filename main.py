from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        if "애란" in data["text"]:
            self.outputs.append([data["channel"], "불렀어?"])
        elif "주사위" == data["text"]:
            die = str(random.randint(1, 6))
            self.outputs.append([data["channel"], die])
        else:
            pass


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
