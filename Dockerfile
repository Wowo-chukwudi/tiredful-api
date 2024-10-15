FROM python:3.9-alpine
LABEL maintainer=woworoseline@gmail.com

COPY requirements.txt /app/

RUN apk add --no-cache python3 python3-dev py3-pip build-base \
    && python3 -m venv /app/venv \
    && /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt
    
COPY . /app

RUN addgroup -g 1000 appgroup && \
    adduser -u 1000 -G appgroup -s /bin/sh -D appuser && \
    chown -R appuser:appgroup /app

WORKDIR /app/Tiredful-API

USER appuser

EXPOSE 8000

CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
