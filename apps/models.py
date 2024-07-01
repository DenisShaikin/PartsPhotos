# from app import db
# from app.settings import BASE_DIR as
import os
import pandas as pd
from flask import current_app as app
from apps import db

class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50))
    article = db.Column(db.String(20))
    name = db.Column(db.String(20))
    url = db.Column(db.String(255))

    def __repr__(self):
        return '"url":"{}"'.format(self.url)

    def load_photos(self):
        def f(brand_, partnum):
            return '\\/' + brand_ + '\\/' + partnum + '.jpg'
        # basedir = os.path.abspath(os.path.dirname(__file__))
        # return
        photos = pd.read_csv(app.config['PHOTOS_FILE'], encoding='utf-8', sep=';')
        photos.url = photos.apply(lambda x: f(x['brand'], x['article']), axis=1)
        print(photos.head())
        print(photos.head())
        print('dbEngine=', db.engine)
        photos.index.name = 'id'
        photos.to_sql('photo', con=db.engine, if_exists='replace', index=False)
        # dtype = {'id': db.Integer}, chunksize = 10000
        return ''