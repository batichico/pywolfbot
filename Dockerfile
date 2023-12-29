FROM python:3.9

WORKDIR /app

RUN pip install errbot[telegram]==6.1.9

COPY . .

CMD ["errbot", "-c", "errbot_config.py"]
