FROM debian
MAINTAINER Andrew Codispoti


RUN apt-get update && apt-get install -y libxml2-dev python3-pip libxslt-dev zlib1g-dev
RUN pip3 install lxml
ENV RDS_HOSTNAME=aa8um8jl3fn77x.ccychmdd3oxe.us-east-1.rds.amazonaws.com
ENV RDS_PORT=3306
ENV RDS_USERNAME=
ENV RDS_PASSWORD=
ENV RDS_DB_NAME=Muzik

ADD . /srv
RUN pip3 install -r /srv/requirements.txt
CMD python3 /srv/app.py
