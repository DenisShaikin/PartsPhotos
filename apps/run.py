# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   flask_migrate import Migrate
from   sys import exit

from config import config_dict
from apps import create_app, db
# from waitress import serve

# WARNING: Don't run with debug turned on in production!
DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG)             )
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)
    print(app_config.SQLALCHEMY_DATABASE_URI)
    # app.logger.info('ASSETS_ROOT = ' + app_config.ASSETS_ROOT )

if __name__ == "__main__":
    HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
    try:
        # Номер порта, на котором запустится веб-приложение
        # выбирается системой случайным образом.
        # В среде ASP.NET номер порта хранится в
        # переменной ASPNETCORE_PORT.
        # PORT = int(os.environ.get('SERVER_PORT', '5789'))
        PORT = int(os.environ.get('ASPNETCORE_PORT', '5000'))
    except ValueError:
        # При ошибке получения порта доступа к веб-приложению
        # определяется порт по умолчанию
        PORT = 5000
    print('HOST={}, PORT={}', HOST, PORT)
    app.run(HOST, PORT)
    # serve(app, host=HOST, port=PORT)
