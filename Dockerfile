FROM ubuntu:latest

# Install dependencies
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install sqlalchemy
RUN pip install psycopg2-binary
RUN pip install pytest==2.9.1

WORKDIR /app

# default entrypoint "/bin/bash -c"