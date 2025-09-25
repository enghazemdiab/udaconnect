FROM python:3.12-alpine

RUN apk add --no-cache build-base gcc musl-dev linux-headers geos libc-dev postgresql-dev postgresql-client python3-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -v -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
