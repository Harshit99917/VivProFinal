from pydantic import BaseModel
from typing import Optional

class Song:
    def __init__(self, id: str, title: str, danceability: float, energy: float,
                 mode: int, acousticness: float, tempo: float,
                 duration_ms: int, num_sections: int, num_segments: int,
                 rating: Optional[int] = None):
        self.id = id
        self.title = title
        self.danceability = danceability
        self.energy = energy
        self.mode = mode
        self.acousticness = acousticness
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.num_sections = num_sections
        self.num_segments = num_segments
        self.rating = rating

