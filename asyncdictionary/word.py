from .meaning import Meaning
from .phonetic import Phonetic


class Word:
    """Represents a ``word``
    This is essentially all the information that a request directly to the API will give you
    """

    __slots__ = ("word", "phonetics", "meanings")

    def __init__(self, data):
        self.word = data[0].get("word")
        self.phonetics = [Phonetic(p) for p in data[0]["phonetics"]]
        self.meanings = [Meaning(d) for d in data[0]["meanings"]]
