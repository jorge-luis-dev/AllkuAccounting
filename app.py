# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from hello import Hello

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from bookapi import *

api.add_resource(Hello, '/hello')
api.add_resource(BookListApi, '/books')
api.add_resource(BookApi, '/book/<int:id_book>')


if __name__ == '__main__':
    app.run()
