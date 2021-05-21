class Phonetic:
    __slots__ = ("text", "audio")

    def __init__(self, data):
        self.text = data.get("text")
        self.audio = data.get("audio")
