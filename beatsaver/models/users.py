from dataclasses import dataclass
from typing import Union


NoneType = type(None)

@dataclass
class UserDiffStats:
    def __init__(self, data):
        self.easy=data["easy"]
        self.expert=data["expert"]
        self.expertPlus=data["expertPlus"]
        self.hard=data["hard"]
        self.normal=data["normal"]
        self.total=data["total"]
    easy: int
    expert: int
    expertPlus: int
    hard: int
    normal: int
    total: int

@dataclass
class UserStats:
    def __init__(self, data):
        self.totalUpvotes=data["totalUpvotes"]
        self.totalDownvotes=data["totalDownvotes"]
        self.totalMaps=data["totalMaps"]
        self.rankedMaps=data["rankedMaps"]
        self.avgBpm=data["avgBpm"]
        self.avgDuration=data["avgDuration"]
        self.avgScore=data["avgScore"]
        self.firstUpload=data["firstUpload"]
        self.lastUpload=data["lastUpload"]
        self.diffStats=UserDiffStats(data["diffStats"])
    totalUpvotes: int
    totalDownvotes: int
    totalMaps: int
    rankedMaps: int
    avgBpm: float
    avgDuration: float
    avgScore: float
    firstUpload: str
    lastUpload: str
    diffStats: UserDiffStats
    

@dataclass
class UserDetail:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.hash=None
        if "hash" in data: # Hashes are a legacy field for old beatsaver accounts
            self.hash=data["hash"]
        self.avatar=data["avatar"]
        self.stats=None
        if "stats" in data:
            self.stats=UserStats(data["stats"])
    id: str
    name: str
    hash: Union[str, NoneType]
    avatar: str
    stats: UserStats