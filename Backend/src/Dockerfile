FROM python:3.11.6-slim-bullseye

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install gcc libpq-dev

WORKDIR /app/backend

COPY requirements.txt /app/backend/requirements.txt

RUN pip install -r requirements.txt

COPY . . /app/backend/
