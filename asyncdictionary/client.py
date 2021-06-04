from typing import Optional

import aiohttp

from .errors import WordNotFound
from .http import HTTPClient
from .meaning import Meaning
from .phonetic import Phonetic
from .word import Word


class Client:
    """The class needed to make requests to the API"""

    __slots__ = ("_http")

    def __init__(self, *, _session: Optional[aiohttp.ClientSession] = None) -> None:
        self._http = HTTPClient(session=_session)


    async def get_response(self, word: str) -> list:
        """A helper method to get the response of the API

        Parameters
        ----------
        word : str
            the word requested

        Returns
        -------
        list
            the response

        Raises
        ------
        WordNotFound
            If the word was not found by the API
        """
        response = await self._http.get("https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word)
        if isinstance(response, dict):
            raise WordNotFound("Sorry pal, we couldn't find definitions for the word you were looking for.")
        return response


    async def get_word(self, word: str) -> Word:
        """A method to get the information of the whole word

        Parameters
        ----------
        word : str
            the word you want the information of

        Returns
        -------
        Word
            A class containing the information
        """
        response = await self.get_response(word)
        return Word(response)


    async def get_meanings(self, word: str) -> list[Meaning]:
        """A method to get just the definitions of a word

        Parameters
        ----------
        word : str
            the word you want the information of.

        Returns
        -------
        list[Meaning]
            a list of a class containing the definitions
        """
        response = await self.get_response(word)
        return [Meaning(m) for m in response[0]['meanings']]


    async def get_phonetics(self, word: str) -> list[Phonetic]:
        """A method to get pronunciation related things of a word

        Parameters
        ----------
        word : str
            the word you want the information of

        Returns
        -------
        list[Phonetic]
            a list of a class containing pronunciations
        """
        response = await self.get_response(word)
        return [Phonetic(p) for p in response[0]["phonetics"]]


    async def get_pronunciations(self, word: str) -> list[Phonetic]:
        """Same thing as ``Client.get_phonetics``"""
        await self.get_phonetics(word)


    async def close(self) -> None:
        """Closes the Client"""
        await self._http.close()
