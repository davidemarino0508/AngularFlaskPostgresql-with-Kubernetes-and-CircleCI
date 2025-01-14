FROM python:3.7.3

MAINTAINER Davide Marino 'info@davidemarino.io'

ARG COMMIT_REF
ARG BUILD_DATE

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app

# Update working directory
WORKDIR /usr/src/app

# copy everything from this directory to server/flask docker container
COPY . /usr/src/app/

# Give execute permission to below file, so that the script can be executed by docker.
RUN chmod 777 /usr/src/app/entrypoint.sh

# Install the Python libraries
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# COPY uswgi.ini
COPY ./uwsgi.ini /etc/uwsgi.ini

ENV APP_COMMIT_REF=${COMMIT_REF} \
    APP_BUILD_DATE=${BUILD_DATE}

EXPOSE 5000

# run server
CMD ["./entrypoint.sh"]