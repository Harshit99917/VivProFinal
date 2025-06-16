from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List

from app.schemas.song_schema import SongSchema, RatingSchema
from app.schemas.response_schema import StandardResponse
from app.services.song_service import SongService
from app.repositories.song_repository import SongRepository
from app.utils.normalizer import normalize_songs

router = APIRouter(prefix="/songs", tags=["Songs"])

repo = SongRepository()
service = SongService(repo)
repo.load_songs(normalize_songs())

@router.get("/", response_model=StandardResponse)
def get_all_songs(skip: int = 0, limit: int = 10):
    try:
        result = service.get_all_songs(skip, limit)
        song_schema_list = [SongSchema(**song.__dict__) for song in result]
        return StandardResponse(status="success", message="Songs fetched", data=song_schema_list)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=StandardResponse(status="error", message=str(e)).dict()
        )

@router.get("/{title}", response_model=StandardResponse)
def get_song_by_title(title: str):
    try:
        song = service.get_song_by_title(title)
        if not song:
            return JSONResponse(
                status_code=404,
                content=StandardResponse(status="error", message="Song not found").dict()
            )
        return StandardResponse(status="success", message="Song found", data=SongSchema(**song.__dict__))
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=StandardResponse(status="error", message=str(e)).dict()
        )

@router.post("/rate", response_model=StandardResponse)
def rate_song(data: RatingSchema):
    try:
        if not (1 <= data.rating <= 5):
            return JSONResponse(
                status_code=400,
                content=StandardResponse(status="error", message="Rating must be between 1 and 5").dict()
            )
        if not service.rate_song(data.title, data.rating):
            return JSONResponse(
                status_code=404,
                content=StandardResponse(status="error", message="Song not found").dict()
            )
        return StandardResponse(
            status="success",
            message="Rating updated",
            data={"title": data.title, "rating": data.rating}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=StandardResponse(status="error", message=str(e)).dict()
        )
