from dateutil import parser

from .base_wrapper import BaseWrapper
from .models.maps import MapDetail
from .models.users import UserDetail


class BeatSaverAsync(BaseWrapper):
    async def get_maps_id(self, id: str) -> MapDetail:
        """Get map information from a map ID"""
        result = await self._async_fetch(f"maps/id/{id}")
        return MapDetail(result)

    async def get_maps_hash(self, hash: str) -> MapDetail:
        """Get map information from a map hash"""
        result = await self._async_fetch(f"maps/hash/{hash}")
        return MapDetail(result)

    async def get_maps_uploader(self, id: str, page: int = 0) -> list:
        """Get maps by a user"""
        result = await self._async_fetch(f"maps/uploader/{id}/{page}")
        maps = list()
        for doc in result["docs"]:
            maps.append(MapDetail(doc))
        return maps

    async def get_maps_latest(self) -> list:
        """Get maps ordered by upload date"""
        result = await self._async_fetch("maps/latest")
        maps = list()
        for doc in result["docs"]:
            maps.append(MapDetail(doc))
        return maps

    async def get_maps_plays(self, page: int = 0 ) -> list:
        """Get maps ordered by play count"""
        result = await self._async_fetch(f"maps/plays/{page}")
        maps = list()
        for doc in result["docs"]:
            maps.append(MapDetail(doc))
        return maps

    async def get_users_id(self, id: int) -> UserDetail:
        """Get user info"""
        result = await self._async_fetch(f"users/id/{id}")
        return UserDetail(result)

    async def post_users_verify(self):
        """Verify user tokens (not implemented)"""
        raise NotImplementedError()

    async def get_search_text(self,  
        page: int = 0,
        automapper: bool = None, 
        chroma: bool = None,
        cinema: bool = None,
        startDate: str = None, # api parameter "from"
        fullspread: bool = None,
        maxBpm: float = None,
        maxDuration: int = None,
        maxNps: float = None,
        maxRating: float = None,
        me: bool = None,
        minBpm: float = None,
        minDuration: int = None,
        minNps: float = None,
        minRating: float = None,
        noodle: bool = None,
        query: str = None, # api parameter "q"
        ranked: bool = None,
        sortOrder: str = "Relevance",
        endDate: str = None, # api parameter "to"
        ) -> list:
    # Only explained a handful of parameters, majority are self-explanatory
        """
        Search for maps
        
        Parameters
        ---
        query: str
            The search query request (e.g. Shiny Happy Days)
        page: int
            The page to return, defaults to 0
        automapper: bool
            Whether the returned maps should include auto generated maps.
            Defaults to None.\n
            True = both user and ai made maps,\n
            False = ai only maps,\n
            None = user only maps.
        chroma: bool
        cinema: bool
        start_date: str
        fullspread: bool
        maxBpm: float
        maxDuration: int
        maxNps: float
        maxRating: float
        me: bool
            Mapping Extensions
        minBpm: float
        minDuration: int
        minNps: float
        minRating: float
        noodle: bool
        query: str
        ranked: bool
        sortOrder: str
            The order to return results. Must be 'Latest', 'Relevance', or 'Rating'.
            Defaults to 'Relevance'
        """
        parameters = locals()
        parameters_url = str()
        maps = list()
        # Could be improved?
        if parameters["query"]:
            parameters["q"] = parameters["query"].replace(" ", "%20")
            del parameters["query"]

        if parameters["startDate"]:
            parsed = parser.parse(parameters["startDate"])
            parameters["from"] = f"{parsed.isoformat()}Z"
            del parameters["startDate"]

        if parameters["endDate"]:
            parsed = parser.parse(parameters["endDate"])
            parameters["to"] = f"{parsed.isoformat()}Z"
            del parameters["endDate"]

        for parameter in parameters:
            if parameter == "self" or parameter == "page" or not parameters[parameter]:
                continue
            parameters_url += f"&{parameter}={parameters[parameter]}"

        result = await self._async_fetch(f"search/text/{page}?{parameters_url[1:]}")
        for doc in result["docs"]:
            maps.append(MapDetail(doc))
        return maps

    async def post_vote(self, hash: str, direction: bool = True):
        """Vote on a map (not implemented)"""
        raise NotImplementedError()
        # https://partner.steamgames.com/doc/webapi/ISteamUserAuth
        # https://partner.steamgames.com/doc/api/ISteamUser#GetAuthSessionTicket
        data = {
            "auth":{
                "oculusId": "",
                "proof": "",
                "steamId": ""
            },
            "direction": direction,
            "hash": hash
        }
        self._post("vote", data)
