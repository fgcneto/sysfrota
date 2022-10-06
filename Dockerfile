FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code


RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install django-bootstrap-v5
RUN pip install django-filter
RUN pip install --upgrade sweetify
RUN pip install psycopg2

COPY . .