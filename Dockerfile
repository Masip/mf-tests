FROM python:3.10-slim-bullseye

WORKDIR tests

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ ./tests


