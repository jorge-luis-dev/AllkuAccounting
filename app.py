# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from controller.transactioncontroller import *
from controller.accountcontroller import *

api.add_resource(AccountListController, '/rest/v1/accounts')
api.add_resource(AccountController, '/rest/v1/accounts/<int:id_account>')
api.add_resource(AccountCodeController, '/rest/v1/accounts/code/<string:code>')
api.add_resource(TransactionListController, '/books')
api.add_resource(TransactionController, '/book/<int:id_book>')


if __name__ == '__main__':
    app.run()
