import logging
import signal
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.song_routes import router

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

app = FastAPI(title="Song Normalization API", version="1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include song routes
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logging.info("FestAPI app is starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("🛑 FastAPI app is shutting down gracefully...")

# Signal handler for OS signals like SIGINT and SIGTERM
def handle_shutdown_signal(signum, frame):
    logging.warning(f"🚨 Received shutdown signal ({signum}). Exiting gracefully...")
    
    sys.exit(0)

signal.signal(signal.SIGINT, handle_shutdown_signal)   # Ctrl+C
signal.signal(signal.SIGTERM, handle_shutdown_signal)  # kill <pid>

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical(" Uncaught exception occurred", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = handle_exception
