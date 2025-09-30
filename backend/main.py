from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import yt_dlp

app = FastAPI()

@app.post("/download")
async def download_video(request: Request):
    data = await request.json()
    url = data.get("url")

    if not url:
        return {"error": "No URL provided"}

    try:
        # Extract video info without downloading
        ydl_opts = {"quiet": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "download_url": info.get("url")  # Direct stream link
        }

    except Exception as e:
        return {"error": str(e)}
