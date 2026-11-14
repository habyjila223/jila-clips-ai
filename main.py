
from fastapi import FastAPI

app = FastAPI(
    title="JILA CLIPS AI",
    description="Independent AI engine for automatic video clipping.",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "service": "JILA CLIPS AI",
        "status": "running",
        "message": "Welcome to JILA CLIPS AI!"
    }


@app.get("/api/health")
def health():
    return {
        "ok": True,
        "service": "JILA CLIPS AI",
        "version": "0.1.0"
    }
