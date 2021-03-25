# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import UniqueConstraint


class Transaction(db.Model):
    __tablename__ = 'acc_transactions'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String, nullable=False)
    numeral = db.Column(db.String, nullable=False)
    date_transaction = db.Column(db.DateTime, nullable=False)
    observation = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    __table_args__ = (UniqueConstraint('code', 'numeral', name='uk_transaction'),)
    # authors = db.relationship('LedgerEntrie',
    #                           backref='ledgerentrie',
    #                           lazy='dynamic',
    #                           cascade="all, delete")

    def __init__(self, code, numeral, date_transaction, observation, status):
        self.code = code
        self.numeral = numeral
        self.date_transaction = date_transaction
        self.observation = observation
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        transaction_data = {
            'id': self.id,
            'code': self.code,
            'numeral': self.numeral,
            'date_transaction': self.date_transaction,
            'observation': self.observation,
            'status': self.status
        }
        return transaction_data
