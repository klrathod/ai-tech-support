import re


def mask_email(text: str):
    return re.sub(r"\S+@\S+", "[EMAIL]", text)
