# BeatSaver.py
An API wrapper for [BeatSaver.com](https://beatsaver.com/) which can handle synchronous or asynchronous GET requests.
### Installing
This library can be installed via pip

    pip install beatsaver.py --upgrade

### Usage
#### Initialization
    from beatsaver.beatsaver import BeatSaver
    
    # While recommended the user_agent parameter isn't required.
    beatsaver = BeatSaver(user_agent="My_Awesome_Program! v0.0.1")
Or for asynchronous requests

    from beatsaver.async_beatsaver import BeatSaverAsync
    
    beatsaver = BeatSaverAsync()
#### Getting map by id *(key)*
    beatsaver.get_maps_id("e970")
    # Returns MapDetail class
#### Getting map by hash
    beatsaver.get_maps_hash("69e494f4a295197bf03720029086fabe6856fbce")
    # Returns MapDetail class
#### Getting maps by uploader
    beatsaver.get_maps_uploader(15293)
    # Returns list of MapDetail
#### Getting latest maps
    beatsaver.get_maps_latest()
    # Returns list of MapDetail
#### Getting maps ordered by play count
    beatsaver.get_maps_plays()
    # Returns list of MapDetail
#### Getting user info
    beatsaver.get_users_id(15293)
    # Returns UserDetail class
#### Searching for maps
    beatsaver.get_search_text(query="Shiny Happy Days")
    # Returns list of MapDetail
    # This function takes a ton of parameters, check it's docstring for them.
### Class Models
#### MapDetail
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
#### MapDetailMetadata
    bpm: float
    duration: int
    songName: str
    songSubName: str
    songAuthorName: str
    levelAuthorName: str
#### MapVersion
    hash: str
    key: Union[str, NoneType]
    state: str
    createdAt: str
    sageScore: int
    diffs: List[MapDifficulty]
    downloadURL: str
    coverURL: str
    previewURL: str
#### MapDifficulty
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
#### MapParitySummary
	errors: int
	warns: int
	resets: int
#### MapStats
    plays: int
    downloads: int
    upvotes: int
    downvotes: int
    score: float
#### UserDetail
    id: str
    name: str
    hash: Union[str, NoneType]
    avatar: str
    stats: UserStats
#### UserStats
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
#### UserDiffStats
    easy: int
    expert: int
    expertPlus: int
    hard: int
    normal: int
    total: int