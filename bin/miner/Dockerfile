FROM python:3.9

WORKDIR /app
COPY . .
RUN python3.9 --version
RUN python3.9 -m pip install poetry
RUN python3.9 -m poetry install


CMD ["poetry", "run", "python3.9", "main.py", "server"]
