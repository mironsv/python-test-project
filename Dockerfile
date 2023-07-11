FROM python:3.11-alpine
WORKDIR /var/app
ENV PYTHONPATH=$PYTHONPATH:/var/app
COPY ./app/ .
COPY ./requirements.txt .
RUN apk add --no-cache librdkafka-dev build-base  linux-headers
RUN pip install -r requirements.txt