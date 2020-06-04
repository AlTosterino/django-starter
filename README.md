# Django Starter Template (Django version 3.1a1)
This repository is for Django project boilerplate. It contains development and production ready environment.

## What this starter offers?
This template offers nice and easy to use Django project.
It has separate settings for deployment and production environments. It contains important additions for developers like `django debug toolbar` or `whitenoise`.
It is easy to run and deploy thanks to `docker` and `docker-compose`
It uses PostgreSQL database in production and SQLite in development out of the box.
For deployment it uses `gunicorn` WSGI Server in Docker

## Prerequisites
* [Python 3.8](https://www.python.org/downloads/release/python-383/)
* [Pipenv](https://pipenv.pypa.io/en/latest/)
* [Docker + docker compose](https://www.docker.com/) -> For fast development and deployment

## Usage

> Note: Core settings like INSTALLED_APPS etc. are inside `core/settings/shared.py`

Clone or download .zip file of this repository.
Then You need to install and activate virtual environment:
* Run `pipenv install --dev`
* Then `pipenv shell`

### Development
Default settings for this project are development settings. Those can be edited in file `core/settings/development.py`

To run Django project with those settings run: `python manage.py runserver`


### Production (Running Django with production settings, to deploy this application look at Running with docker)
> Note: WSGI and ASGI applications will use this settings, to change it edit `asgi.py` or `wsgi.py` and change `DJANGO_SETTINGS_MODULE`


Production settings are using environment variables, to edit this behaviour edit the file `core/settings/development.py`

To run Django project with those settings run: `python manage.py runserver --settings=core.settings.production`

### Running with docker
Firstly change environment variables inside `application.env` and `database.env`

Run and build docker container `docker-compose up -d --build`
Now you will have Django application on port 8000. Open browser and type: `localhost:8000`

## Installed apps
* [Whitenoise](http://whitenoise.evans.io/en/stable/) - Serving static files
* [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - Toolbar for debug purposes
