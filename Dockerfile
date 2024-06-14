FROM python:3.10-alpine3.20

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/django-app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

USER app

COPY --chown=app:app entrypoint.sh .

COPY manage.py .
COPY project/ project/

ENTRYPOINT ["./entrypoint.sh"]
