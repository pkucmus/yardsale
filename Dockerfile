FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

RUN apt update && apt install -y \
    gcc \
    git \
    ;

RUN mkdir /srv/app
WORKDIR /srv/app

COPY requirements /srv/app/requirements
RUN pip install -r requirements/prod.pip

ADD . /srv/app

RUN pip install -I .
