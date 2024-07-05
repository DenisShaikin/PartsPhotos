from flask import jsonify, request
# from flask import current_app as app
from apps.api import blueprint
from apps import db
from apps.models import Photo
from . import blueprint
from flask import current_app as app
import os
import pandas as pd
from os import walk
from .main import func_main

AUTH_KEY = "1234ABCD"

@blueprint.route("/multifinderbrands.php", methods=["POST"])
def multibrands():
    print('Мы здесь!')
    args = request.get_json(force=True)[0]
    brand = args['brand'] if args['brand'] else ''
    article = args['article'] if args['article'] else ''


    filepath = app.config['DOMAIN_NAME'] + '\/static\/' + brand + '\/' + article
    # print(filepath)
    filepath_= os.path.join(app.config['BASEDIR_'], 'apps', 'static')
    print('filepath_=', filepath_)
    f = []
    myDict={}
    df = pd.DataFrame(columns=['src', 'res'])
    f = [dirpath+'/'+ f for (dirpath, dirnames, filenames) in os.walk(filepath_) for f in filenames]
    fList = [{'src':itemf.lower().replace('-', '').replace(' ', ''), 'res':itemf} for itemf in f]
    print(fList)
    df = pd.DataFrame.from_dict(fList)
    # df.index=df['src']
    #Забираем список нужных путей
    dfResult = df.loc[(df['src'].str.contains(brand)) & (df['src'].str.contains(article))]['res']
    print(dfResult.head())
    # собираем список
    ptotosList= []
    for item in dfResult:
        print(item)
        brand_ = item.replace('\\', '/').split('/')[-2]
        article_ = item.replace('\\', '/').split('/')[-1]
        if not '_mini' in article_:
            resLink = app.config['DOMAIN_NAME'] + '\/static\/' + brand_ + '\/' + article_
            # resLink = resLink.replace('\\', r"\")
            ptotosList.append({'url': resLink})
        # if os.path.exists(filepath_+'.jpg'):
        #     ptotosList.append({'url:"': filepath + ".jpg"})
        # for i in range(10):
        #     if os.path.exists(filepath_ + '_' + str(i) + '.jpg'):
        #         ptotosList.append({'"url:"': filepath + '_' + str(i) + '.jpg"'})
        print(ptotosList)
    return (ptotosList)

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