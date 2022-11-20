FROM python:3.10

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /usr/src/app
ADD Pipfile .
ADD Pipfile.lock .

RUN pip install -U pip && \
    pip install pipenv && \
    pipenv install --system --ignore-pipfile --deploy
