## Use slim buster images
#FROM python:3.8.5-slim-buster
#
## Make a working directory
#RUN mkdir /app
#
#WORKDIR /app
#
## First, copy the requirements.txt only as it helps with caching
## Details: https://pythonspeed.com/articles/docker-caching-model/
#COPY ./requirements.txt /app
#RUN pip install -r requirements.txt
#
## Copy the source code
#COPY . /app
#
## Turn of debugging in production
#ENV FLASK_DEBUG 0
#
## Set entrypoint
#ENV FLASK_APP flask_run.py
#ENV FLASK_RUN_HOST 0.0.0.0
#EXPOSE 4000
#
## Run Flask command
#CMD ["gunicorn", "-b", "0.0.0.0:4000", "app.run:application"]

FROM python:3.9.9-slim-bullseye

# Environment variables, setting app home path and copy of the python app in the container
ENV PYTHONUNBUFFERED True

ENV APP_HOME /home/abcpPhotos
WORKDIR $APP_HOME
RUN useradd abcpuser
RUN chown -R abcpuser:abcpuser ./
# ./

COPY . ./

# Update/upgrade the system
RUN apt -y update
RUN apt -y upgrade

copy requirements.txt requirements.txt
# RUN python -m venv venv комментарий
# RUN venv/bin/pip install -r requirements.txt

RUN pip install -r requirements.txt
RUN pip uninstall -y jwt
RUN pip uninstall -y Pyjwt
RUN pip install Pyjwt==1.7.1

RUN pip install gunicorn pymysql

COPY apps apps
#COPY media media
# COPY migrations migrations
COPY boot.sh ./
# COPY thorns.csv wear_discounts.csv TirePricesBase.csv RimPricesBase.csv RimsCatalogue.csv TireGide.csv Areas.csv RossiyaAllTires_Result.csv ./apps
RUN chmod +x boot.sh

ENV FLASK_APP apps
ENV FLASK_ENV Production

RUN chown -R abcpuser:abcpuser /var/log/

USER abcpUser

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
