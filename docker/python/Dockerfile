FROM python:3.8

ARG APP=/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR ${APP}

RUN apt-get update && apt-get install -y --no-install-recommends 

COPY . ${APP}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/app/docker/python/docker-entrypoint.sh" ]

CMD ["runserver"]
