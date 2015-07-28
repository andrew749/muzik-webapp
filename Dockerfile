FROM muzik-env
MAINTAINER Andrew Codispoti

ADD . /srv

ENV RDS_HOSTNAME=aa8um8jl3fn77x.ccychmdd3oxe.us-east-1.rds.amazonaws.com
ENV RDS_PORT=3306
ENV RDS_USERNAME=test
ENV RDS_PASSWORD=test
ENV RDS_DB_NAME=Muzik

EXPOSE 80

CMD python3 /srv/app.py
