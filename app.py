from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import subprocess
import uuid
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Vakyansh TTS API is running!"}

@app.post("/tts")
async def tts(request: Request):
    try:
        data = await request.json()
        text = data.get("input", "")
        lang = data.get("lang", "hi")

        if not text:
            return {"error": "No input text provided"}

        # Output file ka ek unique naam banayein
        output_file = f"output_{uuid.uuid4().hex}.wav"

        # Vakyansh inference script ko call karein
        # Note: Ensure karein ki tts_infer.py vakyansh folder ke andar maujood hai
        subprocess.run([
            "python", "tts_infer.py",
            "--lang", lang,
            "--input", text,
            "--output", output_file
        ], check=True)

        # File check karein aur wapas bhejein
        if os.path.exists(output_file):
            return FileResponse(output_file, media_type="audio/wav")
        else:
            return {"error": "TTS engine failed to generate audio file."}

    except Exception as e:
        return {"error": str(e)}
