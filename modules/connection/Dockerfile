FROM python:3.12-alpine

WORKDIR .

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "wsgi.py"]
