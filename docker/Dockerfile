FROM python:3.8-slim

RUN apt-get update
RUN apt-get install vim -y
RUN pip3 install pytest

WORKDIR /opt/pyflash
COPY . /opt/pyflash
