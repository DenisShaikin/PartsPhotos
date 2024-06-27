from flask import jsonify, request
# from flask import current_app as app
from apps.api import blueprint
from apps import db
from apps.models import Photo
from . import blueprint
from .main import func_main

AUTH_KEY = "1234ABCD"

@blueprint.route("/multifinderbrands.php", methods=["POST"])
def multibrands():

    args = request.get_json(force=True)
    query = db.session.query(Photo.url).filter_by(**args)
    photoLinks = query.all()
    ptotosList= []
    for photo in photoLinks:
        # print(photo)
        ptotosList.append(photo._asdict())
    return str(ptotosList)

@blueprint.route("/<num>", methods=["GET"])
def view(num):

    headers = request.headers
    args = request.args
    print(args)
    query = db.session.query(Photo.url).filter_by(**args)
    photoLinks = query.all()
    # print(tires)
    ptotosList= []
    for photo in photoLinks:
        ptotosList.append(photo._asdict())
    # print(ptotosList)
    return jsonify({ "url": ptotosList[0] if ptotosList else "EMPTY"}), 200

@blueprint.route('/init_database', methods=['GET'])
def init_database():
    # print('first=', Photo.query.get(1))
    if Photo.query.get(1) is None:
        photos = Photo()
        photos.load_photos()
    # if db.session.query.get(1) is None:
    #     # db.session.add_all([ApiSource(source='Avito'), ApiSource(source='Drom')])
    #     db.session.commit()

    return 'Success'