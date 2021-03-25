# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import UniqueConstraint
from models.account import Account
from models.document import Document


class Transaction(db.Model):
    __tablename__ = 'acc_transactions'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String,
                     db.ForeignKey('adm_documents.code'), nullable=False)
    numeral = db.Column(db.String, nullable=False)
    date_transaction = db.Column(db.DateTime, nullable=False)
    observation = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    __table_args__ = (UniqueConstraint('code', 'numeral', name='uk_transaction'),)
    ledger_entries = db.relationship('LedgerEntry',
                              backref='transaction',
                              lazy='dynamic',
                              cascade="all, delete")

    def __init__(self, code, numeral, date_transaction, observation, status):
        self.code = code
        self.numeral = numeral
        self.date_transaction = date_transaction
        self.observation = observation
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        ledgerentry_data = []
        for a in self.ledger_entries.all():
            a_data = {}
            a_data['id'] = a.id
            a_data['accountCode'] = a.account_code
            # Get account name
            account = Account.query.filter_by(code=a.account_code).first()
            a_data['accountName'] = account.name
            a_data['type'] = a.type
            a_data['amount'] = a.amount
            a_data['observation'] = a.observation
            ledgerentry_data.append(a_data)

        # Get document name
        document = Document.query.filter_by(code=self.code).first()
        transaction_data = {
            'id': self.id,
            'code': self.code,
            'codeName': document.name,
            'numeral': self.numeral,
            'date': self.date_transaction,
            'observation': self.observation,
            'status': self.status,
            'ledgerEntries': ledgerentry_data
        }
        return transaction_data
