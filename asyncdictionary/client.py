import aiohttp

from .definition import Definition
from .errors import APIError, WordNotFound
from .http import HTTPClient


class Client:
    
    __slots__ = {"session"}
    
    def __init__(self, session: aiohttp.ClientSession = None):
        self._http = HTTPClient(session)
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"


    def get_url(self, word):
        return self.url + word


    async def get_definitions(self, word: str):
        url = self.get_url(word)
        def_list = []
        response = await self._http.get(url)
        if isinstance(response, dict):
            raise WordNotFound("Sorry, we couldn't find that word for you")
        for definition in response[0]['meanings']:
            d = Definition(definition)
            def_list.append(d)






    async def get_word(word):
        pass
