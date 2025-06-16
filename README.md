# 🎵 Song Normalization API

This FastAPI project normalizes song data from JSON format and exposes a RESTful API to interact with the songs.

---

## 🚀 Setup Instructions

### 1. Clone the Repository or Unzip the Project

```bash
cd song_project_clean
```

### 2. (Recommended) Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

---



---

## 🧪 Run Tests

```bash
PYTHONPATH=./ pytest

 PYTHONPATH=. pytest tests/test_song_service.py
```

---


