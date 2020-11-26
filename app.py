# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from api.transactionapi import *
from api.accountapi import *

api.add_resource(AccountListApi, '/accounts')
api.add_resource(AccountApi, '/account/<int:id_account>')
api.add_resource(AccountCodeApi, '/account_by_code/<string:code>')
api.add_resource(TransactionListApi, '/books')
api.add_resource(TransactionApi, '/book/<int:id_book>')


if __name__ == '__main__':
    app.run()
