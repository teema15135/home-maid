FROM python:3.8

RUN mkdir /app/
RUN mkdir /app/requirements/

COPY requirements/ /app/requirements/
COPY requirements.txt /app/

WORKDIR /app/
RUN pip install -r requirements/local.txt
RUN pip install uWSGI==2.0.19.1

COPY . /app/

WORKDIR /app/homemaid/
RUN python manage.py migrate
# RUN python manage.py collectstatic
ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]