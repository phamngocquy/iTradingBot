FROM python:3.8.13-slim-buster
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
	&& apt-get install -y gcc g++ libpq-dev tzdata \
	&& rm -rf /var/cache/apt/*

RUN mkdir /var/app
WORKDIR /var/app

COPY requirements.txt /var/

RUN pip3 install --no-cache-dir -U pip
RUN pip3 install --no-cache-dir -r /var/requirements.txt

COPY . /var/app

ENV PYTHONPATH=/var/app
