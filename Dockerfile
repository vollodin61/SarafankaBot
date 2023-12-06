FROM python:3.11.5-alpine3.18

RUN apk update && \
    apk add musl-dev libpq-dev gcc

WORKDIR /sarafanka

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
