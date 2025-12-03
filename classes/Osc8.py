import re


class Os8:
    def __init__(self):
        pass

    @staticmethod
    def clear_str(s: str) -> str:
        # выкидываем OSC8-гиперссылки
        OSC8_RE = re.compile(r"\x1b]8;;.*?\x1b\\")
        return OSC8_RE.sub("", s)


# how to use:
# self.searched_pacman = [
#     Os8.clear_str(line) for line in self.searched_pacman if line.strip()
# ]
