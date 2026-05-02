FROM python:3.9

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y git ffmpeg

# Vakyansh repo clone karein
RUN git clone https://github.com/Open-Speech-EkStep/vakyansh-tts.git /app/vakyansh

WORKDIR /app/vakyansh

# Local app.py ko copy karein
COPY app.py .

# Requirements aur Gunicorn/Flask install karein
RUN pip install -r requirements.txt gunicorn flask

EXPOSE 5000

# Gunicorn ke through Flask API run karein
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:app"]
