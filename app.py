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

# Accounts
api.add_resource(AccountListController, '/rest/v1/accounting/accounts')
api.add_resource(AccountController, '/rest/v1/accounting/accounts/<int:id_account>')
api.add_resource(AccountCodeController, '/rest/v1/accounting/accounts/code/<string:code>')
# Transactions
api.add_resource(TransactionListController, '/rest/v1/accounting/transactions')
api.add_resource(TransactionController, '/rest/v1/accounting/transaction/<int:id_transaction>')
api.add_resource(TransactionCodeNumeralController, '/rest/v1/accounting/transaction/code/<string:code>/numeral/<string:numeral>')


if __name__ == '__main__':
    app.run()
