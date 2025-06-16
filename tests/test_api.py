from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_songs():
    response = client.get("/songs/")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert isinstance(json_data["data"], list)

def test_get_song_by_title():
    response = client.get("/songs/3AM")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert "id" in json_data["data"]

def test_rate_song():
    response = client.post("/songs/rate", json={"title": "3AM", "rating": 5})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert json_data["message"] == "Rating updated"
