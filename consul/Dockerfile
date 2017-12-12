FROM consul

ADD . /consul

WORKDIR /consul

EXPOSE 8500

CMD consul agent -dev -client 0.0.0.0

