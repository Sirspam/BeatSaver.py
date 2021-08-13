class BeatSaverNotFound(Exception):
    """Raised when BeatSaver returns Not Found error"""
    pass

class BeatSaverInternalError(Exception):
    """Raised when BeatSaber returns an internal error"""
    pass