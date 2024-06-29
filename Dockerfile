
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

USER abcpuser

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
