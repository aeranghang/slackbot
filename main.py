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
        # 메시지를 말머리(prefix)와 나머지 부분(rest)으로 분리
        prefix, rest = data["text"][:3], data["text"][3:]

        # 말머리가 일치하지 않으면 응답하지 않음
        if prefix != "애란 ":
            return

        # 응답
        reply = answer(rest)
        if reply is not None:
            self.outputs.append([data["channel"], reply])


config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()
