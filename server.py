from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import subprocess
import uuid

app = FastAPI()

@app.post("/tts")
async def tts(request: Request):
    data = await request.json()
    text = data.get("input")
    lang = data.get("lang", "hi")

    # आउटपुट फाइल का नाम
    output_file = f"{uuid.uuid4()}.wav"

    # Vakyansh CLI से ऑडियो जनरेट करें
    subprocess.run([
        "python", "inference.py",
        "--lang", lang,
        "--input", text,
        "--output", output_file
    ])

    return FileResponse(output_file, media_type="audio/wav")
    
