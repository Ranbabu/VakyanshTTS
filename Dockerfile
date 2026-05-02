FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y git ffmpeg

# Vakyansh repo clone करें
RUN git clone https://github.com/Open-Speech-EkStep/vakyansh-tts.git /app/vakyansh

WORKDIR /app/vakyansh

RUN pip install -r requirements.txt fastapi uvicorn

EXPOSE 5000

# हमारी FastAPI app.py को run करें
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
