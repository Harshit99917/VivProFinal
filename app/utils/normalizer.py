import json
from app.models.song_model import Song

def normalize_songs():
    with open("app/data/songs.json", "r") as f:
        data = json.load(f)

    num_items = len(data["id"])
    songs = []
    for i in range(num_items):
        song = Song(
            id=data["id"][str(i)],
            title=data["title"][str(i)],
            danceability=float(data["danceability"][str(i)]),
            energy=float(data["energy"][str(i)]),
            mode=int(data["mode"][str(i)]),
            acousticness=float(data["acousticness"][str(i)]),
            tempo=float(data["tempo"][str(i)]),
            duration_ms=int(data["duration_ms"][str(i)]),
            num_sections=int(data["num_sections"][str(i)]),
            num_segments=int(data["num_segments"][str(i)]),
        )
        songs.append(song)
    return songs
