from flask import Flask, request, send_file
from flask_cors import CORS  # <-- यह नया ऐड किया गया है
import subprocess
import uuid
import os

app = Flask(__name__)
CORS(app)  # <-- यह आपके localhost या किसी भी वेबसाइट को एक्सेस की परमिशन देगा

@app.route("/", methods=["GET"])
def root():
    return {"message": "Vakyansh TTS API is running successfully!"}

@app.route("/tts", methods=["POST"])
def tts():
    try:
        # Request se data nikalna
        data = request.get_json(force=True)
        text = data.get("input", "")
        lang = data.get("lang", "hi")

        if not text:
            return {"error": "No input text provided"}, 400

        # Output audio ke liye ek unique naam banayein
        output_file = f"output_{uuid.uuid4().hex}.wav"

        # Vakyansh TTS engine ko call karein
        subprocess.run([
            "python", "tts_infer.py",
            "--lang", lang,
            "--input", text,
            "--output", output_file
        ], check=True)

        # Agar audio ban gayi hai toh return karein
        if os.path.exists(output_file):
            return send_file(output_file, mimetype="audio/wav")
        else:
            return {"error": "TTS engine failed to generate audio file."}, 500

    except subprocess.CalledProcessError as e:
        return {"error": f"TTS script failed: {str(e)}"}, 500
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
