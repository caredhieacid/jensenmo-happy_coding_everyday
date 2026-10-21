import re


def slugify(title):
    words = re.findall(r"[A-Za-z]+", title.lower())
    return "-".join(words)
