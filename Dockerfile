FROM python:3.7

WORKDIR api_testing/

COPY . api_testing/

RUN cd api_testing; \
    pip install -r requirements.txt; \
    python manage.py makemigrations lists; \
    python manage.py migrate;

EXPOSE 8000

CMD ["python", "api_testing/manage.py", "runserver"]