FROM debian:latest

# RUN apk add python3 py3-pip python3-dev libffi-dev build-base curl
RUN apt update && apt install -y python3 python3-pip python3-venv curl

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
ENV PATH /root/.local/bin:$PATH

WORKDIR /app

# incremental builds go brr
ADD pyproject.toml poetry.lock /app/
RUN poetry install

COPY spotifull.py /app

CMD ["poetry", "run", "python3", "spotifull.py"]
