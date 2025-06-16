import json
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
            self._save_to_file()
            return True
        return False

    def _save_to_file(self):
        data = {
            "id": {},
            "title": {},
            "danceability": {},
            "energy": {},
            "mode": {},
            "acousticness": {},
            "tempo": {},
            "duration_ms": {},
            "num_sections": {},
            "num_segments": {},
            "rating": {}
        }

        for i, song in enumerate(self.songs):
            data["id"][str(i)] = song.id
            data["title"][str(i)] = song.title
            data["danceability"][str(i)] = song.danceability
            data["energy"][str(i)] = song.energy
            data["mode"][str(i)] = song.mode
            data["acousticness"][str(i)] = song.acousticness
            data["tempo"][str(i)] = song.tempo
            data["duration_ms"][str(i)] = song.duration_ms
            data["num_sections"][str(i)] = song.num_sections
            data["num_segments"][str(i)] = song.num_segments
            data["rating"][str(i)] = song.rating if song.rating is not None else 0

        with open("app/data/songs.json", "w") as f:
            json.dump(data, f, indent=4)
