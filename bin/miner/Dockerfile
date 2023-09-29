FROM python:3.9

WORKDIR /app
COPY . .
RUN python3.9 --version
RUN python3.9 -m pip install poetry
RUN python3.9 -m poetry install


#CMD ["python3.9", "main.py", "miner"]
#RUN python3.9 -m poetry run rate_miner/cmd/main.py
CMD ["poetry", "run", "python3.9", "rate_miner/cmd/main.py"]
