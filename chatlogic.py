import random


def reply(text):
    if "애란" in text:
        return "불렀어?"
    elif "주사위" == text:
        die = str(random.randint(1, 6))
        return "주사위를 던졌더니 " + die + " 나왔다."
    else:
        return None
