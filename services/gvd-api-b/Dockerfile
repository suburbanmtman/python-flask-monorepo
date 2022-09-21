FROM python:3.8-slim as builder

WORKDIR /usr/src/app
ENV PYTHONPATH=$PYTHONPATH:/usr/src/app

RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python

COPY ./services/gvd-api-b/pyproject.toml .
COPY ./services/gvd-api-b/poetry.lock .

RUN mkdir -p  ../../lib

COPY ./lib/gvd-lib-2 ../../lib/gvd-lib-2

RUN poetry config virtualenvs.create false
RUN poetry install

# Running image
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./services/gvd-api-b/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/flask /usr/local/bin/flask

CMD ["/usr/src/app/entrypoint.sh"]
