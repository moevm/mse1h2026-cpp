FROM python:3.13

RUN apt update && \
    apt install -y wget \
    libglib2.0-dev \
    libmpc-dev \
    gcc \
    nano \
    file \
    vim

WORKDIR /app

COPY workshop/ ./workshop/

WORKDIR /app/workshop

ENTRYPOINT ["python", "main.py"]
