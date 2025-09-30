from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
import yt_dlp
import os
import uuid

app = FastAPI()

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.get("/")
def home():
    return {"message": "YouTube Downloader API is running 🚀"}

@app.get("/download")
def download_video(url: str = Query(..., description="YouTube video URL")):
    try:
        video_id = str(uuid.uuid4())
        output_path = os.path.join(DOWNLOAD_DIR, f"{video_id}.mp4")

        ydl_opts = {
            "outtmpl": output_path,
            "format": "best",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return FileResponse(output_path, filename="video.mp4")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})