from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import subprocess
import uuid

app = FastAPI()

@app.post("/tts")
async def tts(request: Request):
    data = await request.json()
    text = data.get("input", "")
    lang = data.get("lang", "hi")

    # आउटपुट फ़ाइल का नाम unique रखें
    output_file = f"output_{uuid.uuid4().hex}.wav"

    # Vakyansh inference script को call करें
    subprocess.run([
        "python", "tts_infer.py",
        "--lang", lang,
        "--input", text,
        "--output", output_file
    ])

    return FileResponse(output_file, media_type="audio/wav")
    
