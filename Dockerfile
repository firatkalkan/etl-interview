FROM alpine:3.14

RUN apk update && apk add \
                supervisor \
                dcron \
                py3-pip \
                py3-pandas

RUN pip install  pymongo \
                 dnspython

COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /srv/app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
