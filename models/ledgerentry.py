# -*- coding: utf-8 -*-
from app import db


class LedgerEntry(db.Model):
    __tablename__ = 'acc_ledgers_entries'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    account_code = db.Column(db.String,
                             db.ForeignKey('acc_accounts.code'), nullable=False)
    type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    observation = db.Column(db.String, nullable=False)
    transaction_id = db.Column(db.Integer,
                               db.ForeignKey('acc_transactions.id', ondelete='CASCADE'))

    def __init__(self, account_code, type, amount, observation, transaction_id):
        self.account_code = account_code
        self.type = type
        self.amount = amount
        self.observation = observation
        self.transaction_id = transaction_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        ledgerentry_data = {
            'id': self.id,
            'account_code': self.account_code,
            'type': self.type,
            'amount': self.amount,
            'observation': self.observation,
            'transaction_id': self.transaction_id
        }
        return ledgerentry_data
