# #######
# PROJECT
# #######

FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Dependencies Pillow
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN mv wait-for-it.sh /bin/wait-for-it.sh
RUN ["chmod", "+x", "/bin/wait-for-it.sh"]

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

COPY . /project