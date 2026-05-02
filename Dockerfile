FROM python:3.9

WORKDIR /app

# System dependencies install karein
RUN apt-get update && apt-get install -y git ffmpeg

# Vakyansh repo clone karein
RUN git clone https://github.com/Open-Speech-EkStep/vakyansh-tts.git /app/vakyansh

WORKDIR /app/vakyansh

# Sabse important: Aapki local app.py ko container mein copy karein
COPY app.py .

# Requirements aur zaroori libraries install karein
RUN pip install -r requirements.txt fastapi uvicorn

EXPOSE 5000

# FastAPI app ko run karne ka command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
