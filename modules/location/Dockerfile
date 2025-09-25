FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client gcc python3-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install aniso8601==7.0.0
RUN python3 -m pip install attrs==19.1.0
RUN python3 -m pip install Click==7.0
RUN python3 -m pip install Flask==1.1.1
RUN python3 -m pip install flask-accepts==0.10.0
RUN python3 -m pip install flask-cors==3.0.8
RUN python3 -m pip install Flask-RESTful==0.3.7
RUN python3 -m pip install flask-restplus==0.13.0
RUN python3 -m pip install Flask-Script==2.0.6
RUN python3 -m pip install Flask-SQLAlchemy==2.4.0
RUN python3 -m pip install GeoAlchemy2==0.8.4
RUN python3 -m pip install grpcio==1.56.2
RUN python3 -m pip install grpcio-tools==1.56.2
RUN python3 -m pip install itsdangerous==1.1.0
RUN python3 -m pip install Jinja2==2.11.2
RUN python3 -m pip install jsonschema==3.0.2
RUN python3 -m pip install MarkupSafe==1.1.1
RUN python3 -m pip install marshmallow==3.7.1
RUN python3 -m pip install marshmallow-sqlalchemy==0.23.1
RUN python3 -m pip install psycopg2-binary==2.8.5
RUN python3 -m pip install pyrsistent==0.16.0
RUN python3 -m pip install python-dateutil==2.8.1
RUN python3 -m pip install pytz==2020.1
RUN python3 -m pip install six==1.15.0
RUN python3 -m pip install shapely==1.7.0
RUN python3 -m pip install SQLAlchemy==1.3.19
RUN python3 -m pip install Werkzeug==0.16.1
RUN python3 -m pip install flask-restx==0.2.0
RUN python3 -m pip install protobuf==4.23.4
RUN python3 -m pip install requests==2.31.0
RUN python3 -m pip install gunicorn==20.1.0
RUN python3 -m pip install kafka-python==2.0.2

EXPOSE 5000

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]