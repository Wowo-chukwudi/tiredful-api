FROM alpine:3.20
LABEL maintainer=woworoseline@gmail.com

COPY . /app/

RUN apk add --no-cache \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
  && python3 -m venv /app/venv \
  && /app/venv/bin/pip install --upgrade pip \
  && /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

WORKDIR /app/Tiredful-API

RUN addgroup --gid 1002 tiredgroup \
  && adduser --uid 1002 --ingroup tiredgroup --system --no-create-home tireduser

USER tireduser

EXPOSE 8000/tcp

CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
