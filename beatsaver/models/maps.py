from dataclasses import dataclass
from typing import List, Union

from .users import UserDetail


NoneType = type(None)

@dataclass
class MapDetailMetadata:
    def __init__(self, data):
        self.bpm=data["bpm"]
        self.duration=data["duration"]
        self.songName=data["songName"]
        self.songSubName=data["songSubName"]
        self.songAuthorName=data["songAuthorName"]
        self.levelAuthorName=data["levelAuthorName"]
    bpm: float
    duration: int
    songName: str
    songSubName: str
    songAuthorName: str
    levelAuthorName: str

@dataclass
class MapStats:
    def __init__(self, data):
        self.plays=data["plays"]
        self.downloads=data["downloads"]
        self.upvotes=data["upvotes"]
        self.downvotes=data["downvotes"]
        self.score=data["score"]
    plays: int
    downloads: int
    upvotes: int
    downvotes: int
    score: float

@dataclass
class MapParitySummary:
    def __init__(self, data):
        self.errors=data["errors"]
        self.warns=data["warns"]
        self.resets=data["resets"]
    errors: int
    warns: int
    resets: int

@dataclass
class MapDifficulty:
    def __init__(self, data):
        self.njs=data["njs"]
        self.offset=data["offset"]
        self.notes=data["notes"]
        self.bombs=data["bombs"]
        self.obstacles=data["obstacles"]
        self.nps=data["nps"]
        self.length=data["length"]
        self.characteristic=data["characteristic"]
        self.difficulty=data["difficulty"]
        self.events=data["events"]
        self.chroma=data["chroma"]
        self.me=data["me"]
        self.ne=data["ne"]
        self.cinema=data["cinema"]
        self.seconds=data["seconds"]
        self.paritySummary=MapParitySummary(data["paritySummary"])
        stars = None
        if "stars" in data:
            stars = data["stars"]
        self.stars=stars
    njs: float
    offset: float
    notes: int
    bombs: int
    obstacles: int
    nps: float
    length: float
    characteristic: str
    difficulty: str
    events: int
    chroma: bool
    me: bool
    ne: bool
    cinema: bool
    seconds: float
    paritySummary: MapParitySummary
    stars: Union[float, NoneType]

@dataclass
class MapVersion:
    def __init__(self, data):
        self.hash=data["hash"]
        self.key=None
        # Old maps include the key, new ones don't
        # Because what's consistency? :tf:
        if "key" in data:
            self.key=data["key"]
        self.state=data["state"]
        self.createdAt=data["createdAt"]
        # Same story as the key above
        self.sageScore=None
        if "sageScore" in data:
            self.sageScore=data["sageScore"]
        _diffs = list()
        for diff_data in data["diffs"]:
            _diffs.append(MapDifficulty(diff_data))
        self.diffs=_diffs
        self.downloadURL=data["downloadURL"]
        self.coverURL=data["coverURL"]
        self.previewURL=data["previewURL"]
    hash: str
    key: Union[str, NoneType]
    state: str
    createdAt: str
    sageScore: int
    diffs: List[MapDifficulty]
    downloadURL: str
    coverURL: str
    previewURL: str

@dataclass
class MapDetail:
    def __init__(self, data):
        self.id=data["id"]
        self.name=data["name"]
        self.description=data["description"]
        self.uploader=UserDetail(data["uploader"])
        self.metadata=MapDetailMetadata(data["metadata"])
        self.stats=MapStats(data["stats"])
        self.uploaded=data["uploaded"]
        self.automapper=data["automapper"]
        self.ranked=data["ranked"]
        self.qualified=data["qualified"]
        _versions = list()
        for version_data in data["versions"]:
            _versions.append(MapVersion(version_data))
        self.versions=_versions
    id: str
    name: str
    description: str
    uploader: UserDetail
    metadata: MapDetailMetadata
    stats: MapStats
    uploaded: str
    automapper: bool
    ranked: bool
    qualified: bool
    versions: List[MapVersion]