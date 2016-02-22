FROM debian
MAINTAINER Andrew Codispoti

RUN apt-get update && apt-get install -y libxml2-dev python3-pip libxslt-dev zlib1g-dev

RUN pip3 install  flask
RUN pip3 install  jinja2
RUN pip3 install  lxml
RUN pip3 install  pymysql
RUN pip3 install  python-dateutil

ADD . /

ENV RDS_HOSTNAME=muzik.ccychmdd3oxe.us-east-1.rds.amazonaws.com
ENV RDS_PORT=3306
ENV RDS_USERNAME=muzik_admin
ENV RDS_PASSWORD=muzik-password
ENV RDS_DB_NAME=Muzik

EXPOSE 80

CMD python3 app.py
