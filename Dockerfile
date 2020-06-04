FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install pipenv && pipenv install && pipenv install psycopg2 && pipenv install gunicorn