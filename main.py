from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret


def answer(text):
    if "애란" in text:
        reply = "불렀어??"
    elif "주사위" == text:
        reply = str(random.randint(1, 6))
    else:
        reply = None
    return reply


class HelloPlugin(Plugin):
    def process_message(self, data):
        reply = answer(data["text"])
        if reply is not None:
            self.outputs.append([data["channel"], reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
