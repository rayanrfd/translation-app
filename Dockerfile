FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.7.13 /uv /uvx /bin/

ADD . /app

WORKDIR /app

RUN uv sync --locked

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
