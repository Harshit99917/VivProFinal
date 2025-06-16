from app.repositories.song_repository import SongRepository
from app.models.song_model import Song
from typing import List

class SongService:
    def __init__(self, repo: SongRepository):
        self.repo = repo

    def get_all_songs(self, skip: int, limit: int) -> List[Song]:
        return self.repo.get_all(skip, limit)

    def get_song_by_title(self, title: str) -> Song:
        return self.repo.find_by_title(title)

    def rate_song(self, title: str, rating: int) -> bool:
        return self.repo.update_rating(title, rating)
