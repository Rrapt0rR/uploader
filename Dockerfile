# Dockerfile for Master Portal
#
# Usage:
#
#   docker build -t master-portal .
#   docker run -it -p 5000:5000 master-portal

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    postgresql-client \
    libpq-dev \
    python-dev \
    python-pip \
    libffi-dev

COPY . /master
WORKDIR /master
RUN pip install --upgrade pip -r requirements.txt

EXPOSE 5000

CMD ["/master/bin/run-dev.sh"]