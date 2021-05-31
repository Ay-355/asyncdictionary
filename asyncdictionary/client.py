from typing import Optional

import aiohttp

from .definition import Definition
from .errors import WordNotFound
from .http import HTTPClient
from .meaning import Meaning
from .phonetic import Phonetic
from. word import Word


class Client:

    __slots__ = ("_http")

    def __init__(self, *, _session: Optional[aiohttp.ClientSession] = None) -> None:
        self._http = HTTPClient(session=_session)


    async def get_response(self, word: str) -> list:
        response = await self._http.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)
        if isinstance(response, dict):
            raise WordNotFound("Sorry pal, we couldn't find definitions for the word you were looking for.")
        return response


    async def get_word(self, word: str) -> Word:
        response = await self.get_response(word)
        return Word(response)


    async def get_meanings(self, word: str) -> list[Meaning]:
        response = await self.get_response(word)
        return [Meaning(m) for m in response[0]['meanings']]


    async def get_phonetics(self, word: str) -> list[Phonetic]:
        response = await self.get_response(word)
        return [Phonetic(p) for p in response[0]["phonetics"]]


    async def get_pronunciations(self, word: str) -> list[Phonetic]:
        await self.get_phonetic(word)


    async def close(self) -> None:
        await self._http.close()
