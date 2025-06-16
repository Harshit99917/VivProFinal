from typing import List, Optional
from app.models.song_model import Song

class SongRepository:
    def __init__(self):
        self.songs: List[Song] = []

    def load_songs(self, songs: List[Song]):
        self.songs = songs

    def get_all(self, skip: int = 0, limit: int = 10) -> List[Song]:
        return self.songs[skip:skip+limit]

    def find_by_title(self, title: str) -> Optional[Song]:
        return next((s for s in self.songs if s.title.lower() == title.lower()), None)

    def update_rating(self, title: str, rating: int) -> bool:
        song = self.find_by_title(title)
        if song:
            song.rating = rating
            return True
        return False
