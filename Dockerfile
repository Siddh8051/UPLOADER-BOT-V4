FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y ffmpeg aria2 git wget pv jq python3-dev mediainfo && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install --force-reinstall brotli

RUN pip uninstall -y yt-dlp && \
    pip install yt-dlp && \
    pip install --upgrade yt-dlp

COPY . .

RUN python3 -m pip check yt-dlp

RUN yt-dlp --version

CMD ["sh", "-c", "python3 healthcheck.py & python3 bot.py"]
EXPOSE 8080
EXPOSE 8080
ENV MEMORY="512m"

