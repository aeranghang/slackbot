from rtmbot import RtmBot
from rtmbot.core import Plugin

import secret
import chatlogic


class HelloPlugin(Plugin):
    def process_message(self, data):
        answer = chatlogic.reply(data["text"])
        if answer is None:
            pass
        else:
            self.outputs.append([data["channel"], answer])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
