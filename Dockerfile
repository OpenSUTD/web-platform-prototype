FROM python:3.6.8-slim-stretch
LABEL maintainer="Timothy Liu <timothy_liu@mymail.sutd.edu.sg>"

USER root
ENV DEBIAN_FRONTEND noninteractive

# Install OS dependencies

RUN apt-get update && \
    apt-get install -yq --no-install-recommends --no-upgrade \
    apt-utils && \
    apt-get install -yq --no-install-recommends --no-upgrade \
    build-essential \
    graphviz \
    libgraphviz-dev \
    pkg-config \
    curl \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# install Python dependencies

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    pip install --upgrade --no-cache-dir -r requirements.txt && \
    rm -rf get-pip.py ~/.cache

EXPOSE 8000
