from asyncio import get_event_loop
from os.path import basename

from aiohttp import ClientSession
from requests import get, post

from . import beatsaver_exceptions


class BaseWrapper():
    def __init__(self, user_agent = None):
        self.base_url = "https://beatsaver.com/api"
        self.event_loop = get_event_loop()
        self.user_agent = user_agent or basename(__file__)

    def _fetch(self, endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        response = get(url, headers={"user_agent": self.user_agent})
        if response.status_code == 200:
            return response.json()
        else:
            if "Not Found" in response.text:
                raise beatsaver_exceptions.BeatSaverNotFound()
            if "Internal Server Error" in response.text:
                raise beatsaver_exceptions.BeatSaverInternalError()
            raise BaseException(response.text)

    def _post(self, endpoint: str, data: dict):
        url = f"{self.base_url}/{endpoint}"
        return post(url, json=data, headers={"user_agent": self.user_agent})

    async def _async_fetch(self, endpoint: str):
        url = f"{self.base_url}/{endpoint}"
        async with ClientSession(loop=self.event_loop, headers={"user_agent": self.user_agent}) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    if "Not Found" in await response.text():
                        raise beatsaver_exceptions.BeatSaverNotFound()
                    if "Internal Server Error" in await response.text():
                        raise beatsaver_exceptions.BeatSaverInternalError()
                    raise BaseException(await response.text())

    async def _async_post(self, endpoint: str, data: dict):
        url = f"{self.base_url}/{endpoint}"
        async with ClientSession(loop=self.event_loop, headers={"user_agent": self.user_agent}) as session:
            async with session.post(url, data) as response:
                return response