# -*- coding: utf-8 -*-
from app import db


class LedgerEntrie(db.Model):
    __tablename__ = 'acc_ledger_entries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    transaction_id = db.Column(db.Integer,
                               db.ForeignKey('acc_transactions.id', ondelete='CASCADE'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
