FROM python:3.13-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPYCACHEPREFIX=/tmp/pycache

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

WORKDIR /app
COPY . .
RUN uv sync

ENV PYTHONPATH=/app
