from pydantic import BaseModel
from typing import Optional

class SongSchema(BaseModel):
    id: str
    title: str
    danceability: float
    energy: float
    mode: int
    acousticness: float
    tempo: float
    duration_ms: int
    num_sections: int
    num_segments: int
    rating: Optional[int] = None

class RatingSchema(BaseModel):
    title: str
    rating: int
