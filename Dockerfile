FROM debian/jessie
MAINTAINER Andrew Codispoti


RUN apt-get install libxml2-devel python34-pip libxslt-devel
RUN pip-3.4 install lxml
ENV RDS_HOSTNAME=aa8um8jl3fn77x.ccychmdd3oxe.us-east-1.rds.amazonaws.com
ENV RDS_PORT=3306CMD
ENV RDS_USERNAME=
ENV RDS_PASSWORD=
ENV RDS_DB_NAME=Muzik


CMD python3 app.py
