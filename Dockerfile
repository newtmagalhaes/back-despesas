FROM python:3.10-alpine3.20

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/django-app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY manage.py .
COPY project/ project/
COPY api/ api/

ENTRYPOINT ["./entrypoint.sh"]
