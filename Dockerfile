FROM ubuntu:22.04

RUN apt update && \
    apt install -y wget \
                   libglib2.0-dev \
                   libmpc-dev \
                   gcc \
                   nano \
                   file \
                   vim

WORKDIR /app
# COPY requirements.txt requirements.txt
# Install requirements to cache them in docker layer
# RUN pip3 install -r requirements.txt
COPY README.md ./
COPY ./workshop ./workshop
ENTRYPOINT ["bash"]
