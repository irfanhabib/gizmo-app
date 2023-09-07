FROM python:3.10-slim
LABEL maintainer="irfan@irfanhabib.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Poetry
ENV POETRY_HOME /app/.local
ENV PATH $POETRY_HOME/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 - ;

# Install dependencies first to cache the layer
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

# Copy the rest, which is subject to frequent change, therefore, will be rebuilt repeatedly
COPY . .

CMD ["python", "./your_crawler_script_name.py"]
