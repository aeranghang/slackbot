from rtmbot import RtmBot
from rtmbot.core import Plugin

from chatlogic import answer
import secret


class HelloPlugin(Plugin):
    def process_message(self, data):
        # 메시지를 말머리(prefix)와 나머지 부분(rest)으로 분리
        len_prefix = len(config["PREFIX"])
        prefix, rest = data["text"][:len_prefix], data["text"][len_prefix:]

        # 말머리가 일치하지 않으면 응답하지 않음
        if prefix != config["PREFIX"]:
            return

        # 응답
        reply = answer(rest)
        if reply is not None:
            self.outputs.append([data["channel"], reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "PREFIX": "애란 ",
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
