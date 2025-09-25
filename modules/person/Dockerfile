FROM python:3.12-alpine

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev libffi-dev libpq python3-dev build-base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]