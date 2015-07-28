FROM debian
MAINTAINER Andrew Codispoti

RUN apt-get update && apt-get install -y libxml2-dev python3-pip libxslt-dev zlib1g-dev
ADD requirements.txt /srv/requirements.txt

RUN pip3 install  flask
RUN pip3 install  jinja2
RUN pip3 install  lxml
RUN pip3 install  pymysql
RUN pip3 install  python-dateutil

ADD . /srv

ENV RDS_HOSTNAME=aa8um8jl3fn77x.ccychmdd3oxe.us-east-1.rds.amazonaws.com
ENV RDS_PORT=3306
ENV RDS_USERNAME=andrew749
ENV RDS_PASSWORD=Joseph749
ENV RDS_DB_NAME=Muzik

EXPOSE 80

CMD python3 /srv/app.py
