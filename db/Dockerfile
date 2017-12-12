FROM python:3.6.3

ADD . /sqliteserver

WORKDIR /sqliteserver

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python sqlite_server.py