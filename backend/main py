from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/download")
async def download_video(video: VideoRequest):
    url = video.url
    ydl_opts = {"format": "best", "quiet": True}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            download_url = info["url"]
            title = info.get("title", "Unknown Title")
            thumbnail = info.get("thumbnail", "")

        return {
            "download_url": download_url,
            "title": title,
            "thumbnail": thumbnail
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
