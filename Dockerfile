FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y git ffmpeg

# Vakyansh repo clone करें
RUN git clone https://github.com/Open-Speech-EkStep/vakyansh-tts /app/vakyansh

WORKDIR /app/vakyansh

RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn

EXPOSE 5000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "5000"]
