from typing import Optional

import aiohttp

from .definition import Definition
from .errors import WordNotFound
from .http import HTTPClient
from .meaning import Meaning
from .phonetic import Phonetic


class Client:

    __slots__ = ("_http")

    def __init__(self, *, _session: Optional[aiohttp.ClientSession] = None):
        self._http = HTTPClient(session=_session)


    def get_url(self, word):
        return "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word


    async def get_meanings(self, word: str):
        response = await self._http.get(self.get_url(word))
        if isinstance(response, dict):
            raise WordNotFound("Sorry pal, we couldn't find definitions for the word you were looking for.")
        return [Meaning(m) for m in response[0]['meanings']]


    async def get_word(word):
        pass


    async def close(self):
        await self._http.close()
