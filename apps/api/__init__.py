from flask import Blueprint

blueprint = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static",  url_prefix=''
)

from . import views  # isort:skip
