class Phonetic:
    """Contains text and audio information related to the phonetics of a word"""

    __slots__ = ("text", "audio")

    def __init__(self, data):
        self.text = data.get("text")
        self.audio = data.get("audio")
