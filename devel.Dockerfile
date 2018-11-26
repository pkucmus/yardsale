FROM python:3.7-slim-stretch

ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

RUN apt update && apt install -y \
    gcc \
    git \
    make \
    python-setuptools \
    python-dev \
    libncurses5-dev \
    ;

RUN mkdir /srv/app
WORKDIR /srv/app

ADD ./python-snipeit-client /srv/python-snipeit-client
ADD ./django-classified /srv/django-classified

COPY requirements /srv/app/requirements
RUN pip install -r requirements/devel.pip

ADD . /srv/app

RUN pip install -I -e .
