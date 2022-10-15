FROM python:3.8.14-bullseye

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python - --version 1.2.2

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /usr/colornet_app

COPY pyproject.toml poetry.lock ./
COPY colornet ./colornet

RUN ls -a

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

COPY ./ ./

EXPOSE 80
