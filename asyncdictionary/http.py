from typing import Any, Optional

import aiohttp

from .errors import APIError, WordNotFound


class HTTPClient:

    __slots__ = "session"

    def __init__(self, *, session: Optional[aiohttp.ClientSession] = None) -> None:
        self.session = session or aiohttp.ClientSession()

    async def get(self, url: str, **kwargs) -> Any:
        async with self.session.get(url, timeout=aiohttp.ClientTimeout(60), **kwargs) as res:
            if not 300 >= res.status >= 200:
                if res.status == 404:
                    raise WordNotFound("Sorry pal, we couldn't find definitions for the word you were looking for.")
                else:
                    raise APIError(res.status, await res.text())

            try:
                data = await res.json()
            except aiohttp.ClientResponseError:
                data = await res.read()

        return data

    async def close(self) -> None:
        if self.session:
            await self.session.close()
