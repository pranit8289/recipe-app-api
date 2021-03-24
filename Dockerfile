FROM python:3.7-alpine

ENV PYTHONUNBUFFERD 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

#creating new user itachi
RUN adduser -D itachi
USER itachi
