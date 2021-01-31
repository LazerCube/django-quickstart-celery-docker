# #######
# PROJECT
# #######

FROM python:3.9.0-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG requirements=requirements/production.txt

# Dependencies Pillow
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libpq-dev gcc

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN mv wait-for-it.sh /bin/wait-for-it.sh
RUN ["chmod", "+x", "/bin/wait-for-it.sh"]

COPY requirements/ ./requirements/

RUN pip3 install --upgrade pip
RUN pip3 install -r $requirements
# RUN pip3 install --no-cache-dir -r $requirements

COPY . /project