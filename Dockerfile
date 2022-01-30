FROM python:3.10

COPY requirements/ /tmp/
RUN pip install --upgrade pip
RUN pip install -r /tmp/app.txt -r /tmp/dev.txt

WORKDIR /src
