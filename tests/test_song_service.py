from unittest.mock import MagicMock
from app.services.song_service import SongService
from app.models.song_model import Song

def test_get_all_songs():
    mock_repo = MagicMock()
    mock_repo.get_all.return_value = [
        Song(
            id="1",
            title="Test Song",
            danceability=0.5,
            energy=0.7,
            mode=1,
            acousticness=0.1,
            tempo=120.0,
            duration_ms=200000,
            num_sections=4,
            num_segments=8
        )
    ]
    service = SongService(mock_repo)
    songs = service.get_all_songs(0, 10)
    assert len(songs) == 1
    assert songs[0].title == "Test Song"

def test_get_song_by_title():
    mock_repo = MagicMock()
    mock_repo.find_by_title.return_value = Song(
        id="2",
        title="Another Song",
        danceability=0.6,
        energy=0.8,
        mode=0,
        acousticness=0.2,
        tempo=130.0,
        duration_ms=210000,
        num_sections=5,
        num_segments=10
    )
    service = SongService(mock_repo)
    song = service.get_song_by_title("Another Song")
    assert song.title == "Another Song"

def test_rate_song_success():
    mock_repo = MagicMock()
    mock_repo.update_rating.return_value = True
    service = SongService(mock_repo)
    success = service.rate_song("Some Song", 4)
    assert success is True

def test_rate_song_failure():
    mock_repo = MagicMock()
    mock_repo.update_rating.return_value = False
    service = SongService(mock_repo)
    success = service.rate_song("Nonexistent Song", 5)
    assert success is False
