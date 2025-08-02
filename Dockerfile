FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.8.4 /uv /uvx /bin/

ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app

RUN uv sync --locked

CMD ["uv", "run","uvicorn", "app.main:app", "--reload"]
