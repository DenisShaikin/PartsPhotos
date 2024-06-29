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

# Ставим powershell
# Update the list of packages
# RUN sudo apt-get update
# Install pre-requisite packages.
#RUN apt install -y wget apt-transport-https software-properties-common
## Download the Microsoft repository GPG keys
#RUN wget -q "https://packages.microsoft.com/config/debian/11/packages-microsoft-prod.deb"
## Register the Microsoft repository GPG keys
#RUN dpkg -i packages-microsoft-prod.deb
## Delete the the Microsoft repository GPG keys file
#RUN rm packages-microsoft-prod.deb
## Update the list of packages after we added packages.microsoft.com
#RUN apt update
# Install PowerShell
#RUN apt install -y powershell
# Start PowerShell
# pwsh

#RUN apt -y update
#RUN apt -y upgrade

#RUN apt install -y redis
#RUN apt install -y netcat
#RUN apt install -y cron

#RUN apt -y update
#RUN apt -y upgrade
#
#RUN apt install -y unzip xvfb libxi6 libgconf-2-4

# Install App dependencies and chrome webdriver
#RUN apt install -yqq unzip curl wget python3-pip
#RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN apt install -y --no-install-recommends ./google-chrome-stable_current_amd64.deb
#RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
#RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# WORKDIR /home/rezinos

copy requirements.txt requirements.txt
# RUN python -m venv venv комментарий
# RUN venv/bin/pip install -r requirements.txt

RUN pip install -r requirements.txt
RUN pip uninstall -y jwt
RUN pip uninstall -y Pyjwt
RUN pip install Pyjwt==1.7.1

RUN pip install gunicorn pymysql

COPY apps apps
COPY media media
# COPY migrations migrations
COPY run.py boot.sh ./
# COPY thorns.csv wear_discounts.csv TirePricesBase.csv RimPricesBase.csv RimsCatalogue.csv TireGide.csv Areas.csv RossiyaAllTires_Result.csv ./apps
RUN chmod +x boot.sh

ENV FLASK_APP run.py
ENV FLASK_ENV Production

RUN chown -R abcpUser:abcpUser ./
RUN chown -R abcpUser:abcpUser /var/log/


USER abcpUser

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
