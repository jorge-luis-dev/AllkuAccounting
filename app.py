# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from api.bookapi import *

api.add_resource(BookListApi, '/books')
api.add_resource(BookApi, '/book/<int:id_book>')


if __name__ == '__main__':
    app.run()
