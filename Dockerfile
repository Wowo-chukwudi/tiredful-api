#Official base image. Alpine to reduce attack surface
FROM python:3.9-alpine
LABEL maintainer=woworoseline@gmail.com

#Copied only requirements first to help with caching
COPY requirements.txt /app/

#Install packages, create virtual env and install requirements
RUN apk add --no-cache python3 python3-dev py3-pip build-base \
    && python3 -m venv /app/venv \
    && /app/venv/bin/pip install --upgrade pip \
    && /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt
    
#Copied the rest of the app
COPY . /app

#Created non-root user
RUN addgroup -g 1000 appgroup && \
    adduser -u 1000 -G appgroup -s /bin/sh -D appuser && \
    chown -R appuser:appgroup /app

WORKDIR /app/Tiredful-API

#Switched to non-root user
USER appuser

EXPOSE 8000

CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
