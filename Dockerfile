FROM python:3.8-slim

RUN mkdir /app/
RUN mkdir /app/requirements/

COPY requirements/ /app/requirements/
COPY requirements.txt /app/

WORKDIR /app/
RUN pip install -r requirements/local.txt

COPY . /app/

WORKDIR /app/homemaid/
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver"]