FROM python:3.12-alpine

WORKDIR .


RUN apt-get update && apt-get install -y \ build-essential \ libpq-dev \ && rm -rf /var/lib/apt/lists/*

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]