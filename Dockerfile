FROM python:3.7

RUN mkdir -p app
COPY . /app/

WORKDIR /app
VOLUME /app