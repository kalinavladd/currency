FROM python:3.8

WORKDIR /code/build

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get -y install python3-pip
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH /code/build/app

CMD ["uwsgi", "--http-socket", "0.0.0.0:8000", "--module", "settings.wsgi", "--threads", "2", "--workers", "4"]