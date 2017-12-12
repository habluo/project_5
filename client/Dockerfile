FROM python:3.6.3

ADD . /client

WORKDIR /client

RUN pip install -r requirements.txt

CMD python sqlite_client.py