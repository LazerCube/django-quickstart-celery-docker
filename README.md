# Django + Ngnix + Celery + Docker
[![Build Status](https://travis-ci.org/LazerCube/django-quickstart-celery-docker.svg?branch=master)](https://travis-ci.org/LazerCube/django-quickstart-celery-docker)

**Django** 3.0.x
**Python** 3.9

## Prerequisites

- [Docker Machine](https://docs.docker.com/machine/install-machine/) - For running on mac and windows machines.
- [Docker](https://docs.docker.com/install/) - Runs either with Docker machine or on a linux machine.

## Getting started

To run the app, `docker` and `docker-compose` must be installed on your system. For installation
instructions refer to the Docker [docs](https://docs.docker.com/compose/install/).

### Docker machine (skip if not applicable)

1. Start new machine - `docker-machine create -d virtualbox dev;`
1. Configure your shell to use the new machine environment - `eval $(docker-machine env dev)`

**Note:** For Docker terminal on vscode, windows use `eval $(docker-machine env dev --shell bash)`

#### Add Enviroment File

Create a `.env` file in the root of the project for any enviroment variables for the project.

Example config:

```.gitignore
# Add Environment Variables

COMPOSE_PROJECT_NAME=quickstart

SECRET_KEY=aaabbbccc
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
DB_SERVICE=postgres
DB_PORT=5432

#RABBITMQ_ERLANGCOOKIE=SWQOKODSQALRPCLNMEQG
RABBITMQ_DEFAULT_USER=rabbitmq
RABBITMQ_DEFAULT_PASS=rabbitmq
RABBITMQ_DEFAULT_VHOST=vhost1

DJANGO_LOG_LEVEL=DEBUG
```

#### Compose

The app can be run in development mode using Django's built in web server simply by executing

```bash
docker-compose up
```

To remove all containers in the cluster use

```bash
docker-compose down
```

To run the app in production mode, using gunicorn as a web server and nginx as a proxy, the
corresponding commands are

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
```

#### Swarm

It's also possible to use the same compose files to run the services using docker swarm. Docker
swarm enables the creation of multi-container clusters running in a multi-host environment with
inter-service communication across hosts via overlay networks.

```bash
docker swarm init --advertise-addr 127.0.0.1:2377
docker stack deploy -c docker-compose.yaml -c docker-compose.prod.yaml proj
```

It should be noted that the app will not be accessible via `localhost` in Chrome/Chromium. Instead
use `127.0.0.1` in Chrome/Chromium.

To bring down the project or _stack_ and remove the host from the swarm

```bash
docker stack rm proj
docker swarm leave --force
```

### Getting internal ip

In order to view in a web browser you to grab the docker-machine ip.

```bash
docker-machine ip dev
```

### Useful Commands

- `docker-compose logs -f <container>` - Set terminal to view and follow logs for specified container.

## Running the tests

Explain how to run the automated tests for this system

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python-pip](https://pypi.python.org/pypi/pip) - Dependency Management
- [Nginx](https://www.nginx.com/resources/wiki/) - Open-source, high-performance HTTP server
- [Gunicorn](http://gunicorn.org/) - Python WSGI HTTP Server for UNIX
- [Docker](https://www.docker.com/) - Securely build, share and run any application, anywhere.
- [Celery](http://www.celeryproject.org/) - Asynchronous task queue/job queue based on distributed message passing.
- [RabbitMQ](https://www.rabbitmq.com/) - Open source message broker
- [Wait-For-it](https://github.com/vishnubob/wait-for-it) - Bash script to test and wait on the availability of a TCP host and port
