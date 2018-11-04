FROM python:3.7-alpine3.7

ENV PYTHONUNBUFFERED 1

RUN apk --no-cache add \
    bash \
    gettext \
    jpeg-dev \
    zlib-dev \
    postgresql-dev \
    libffi-dev ;

RUN mkdir /srv/app
WORKDIR /srv/app

RUN set -ex \
    && apk --no-cache add --virtual .build-deps \
        gcc \
        git \
        libc-dev \
        linux-headers \
        make \
        musl-dev \
        ncurses-dev;

COPY requirements /srv/app/requirements
RUN pip install -r requirements/devel.pip

ADD . /srv/app

RUN pip install -I -e .

RUN apk del .build-deps
