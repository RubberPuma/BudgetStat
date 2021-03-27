FROM python:3.8.5

ENV PYTHONUNBUFFERED=1

RUN useradd -ms /bin/bash docker-user

WORKDIR /code

COPY ./code/requirements.txt .

RUN pip install -r requirements.txt

COPY ./code .

RUN chown -R docker-user:docker-user /code
USER docker-user