import random


def answer(text):
    if "애란" in text:
        reply = "불렀어??"
    elif "주사위" == text:
        reply = str(random.randint(1, 6))
    else:
        reply = None
    return reply
