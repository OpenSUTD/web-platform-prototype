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

ENV SHELL=/bin/bash \
    NB_UID=1000 \
    NB_GID=100 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

WORKDIR /app

RUN groupadd wheel -g 11 && \
    echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    useradd -m -s /bin/bash -N -u 1000 opensutd && \
    chown opensutd:$NB_GID /app && \
    chmod g+w /etc/passwd

# install Python dependencies

COPY . /app

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    pip install --upgrade --no-cache-dir -r requirements.txt && \
    rm -rf get-pip.py ~/.cache

USER root

EXPOSE 8000
