
from asyncdictionary.definition import Definition


class Meaning:
    __slots__ = ("part_of_speech", "definitions")

    def __init__(self, data):
        self.part_of_speech = data.get("partOfSpeech")
        self.definitions = [Definition(d) for d in data.get("definitions")]
