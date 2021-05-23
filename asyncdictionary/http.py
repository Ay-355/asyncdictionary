from typing import Optional

import aiohttp

from .errors import APIError


class HTTPClient:
    
    # __slots__ = ("session")
    
    def __init__(self, *, session: Optional[aiohttp.ClientSession] = None):
        self.session = session or aiohttp.ClientSession()


    async def get(self, url, **kwargs):
        async with self.session.get(url, **kwargs) as res:
            if not 300 >= res.status >= 200:
                raise APIError(f"{res.status}: Request was fine but there was an error")

            try:
                data = await res.json()
            except aiohttp.ClientResponseError:
                data = await res.read()

            return data


    async def close(self):
        self.session.close()
