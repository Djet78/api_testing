FROM python:3.7

WORKDIR api_testing/

COPY . .

RUN pip install -r requirements.txt; \
    python manage.py makemigrations lists; \
    python manage.py migrate;
