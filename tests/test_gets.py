import pytest
from beatsaver.beatsaver import BeatSaver
from beatsaver.async_beatsaver import BeatSaverAsync
from beatsaver.beatsaver_exceptions import BeatSaverNotFound


@pytest.fixture
def beatsaver_class():
    return BeatSaver()

def test_get_maps_id(beatsaver_class):
    assert beatsaver_class.get_maps_id("e970") is not None

def test_get_maps_id_not_found(beatsaver_class):
    with pytest.raises(BeatSaverNotFound):
        beatsaver_class.get_maps_id("abcdefgh") # Might actually become a valid beatmap if enough time is given

def test_get_maps_hash(beatsaver_class):
    assert beatsaver_class.get_maps_hash("69e494f4a295197bf03720029086fabe6856fbce") is not None

def test_get_maps_hash_not_found(beatsaver_class):
    with pytest.raises(BeatSaverNotFound):
        beatsaver_class.get_maps_hash("awesome_hash")

def test_get_maps_uploader(beatsaver_class):
        assert beatsaver_class.get_maps_uploader(15293) is not None

def test_get_maps_latest(beatsaver_class):
        assert beatsaver_class.get_maps_latest() is not None

def test_get_maps_plays(beatsaver_class):
        assert beatsaver_class.get_maps_plays() is not None

def test_get_users_id(beatsaver_class):
    assert beatsaver_class.get_users_id(15293) is not None

def test_get_search_text(beatsaver_class):
    assert beatsaver_class.get_search_text(query="Shiny Happy Days") is not None


@pytest.fixture
def async_beatsaver_class():
    return BeatSaverAsync()

@pytest.mark.asyncio
async def test_async_get_maps_id(async_beatsaver_class):
    assert await async_beatsaver_class.get_maps_id("e970") is not None

@pytest.mark.asyncio
async def test_async_get_maps_id_not_found(async_beatsaver_class):
    with pytest.raises(BeatSaverNotFound):
        await async_beatsaver_class.get_maps_id("abcdefgh") # Might actually become a valid beatmap if enough time is given

@pytest.mark.asyncio
async def test_async_get_maps_hash(async_beatsaver_class):
    assert await async_beatsaver_class.get_maps_hash("69e494f4a295197bf03720029086fabe6856fbce") is not None

@pytest.mark.asyncio
async def test_async_get_maps_hash_not_found(async_beatsaver_class):
    with pytest.raises(BeatSaverNotFound):
        await async_beatsaver_class.get_maps_hash("awesome_hash")

@pytest.mark.asyncio
async def test_async_get_maps_uploader(async_beatsaver_class):
        assert await async_beatsaver_class.get_maps_uploader(15293) is not None

@pytest.mark.asyncio
async def test_async_get_maps_latest(async_beatsaver_class):
        assert await async_beatsaver_class.get_maps_latest() is not None

@pytest.mark.asyncio
async def test_async_get_maps_plays(async_beatsaver_class):
        assert await async_beatsaver_class.get_maps_plays() is not None

@pytest.mark.asyncio
async def test_async_get_users_id(async_beatsaver_class):
    assert await async_beatsaver_class.get_users_id(15293) is not None

@pytest.mark.asyncio
async def test_async_get_search_text(async_beatsaver_class):
    assert await async_beatsaver_class.get_search_text(query="Shiny Happy Days") is not None