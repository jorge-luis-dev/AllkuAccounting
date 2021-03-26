# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import UniqueConstraint


class Automatic(db.Model):
    # Is used to save automatics ledger entries
    __tablename__ = 'acc_automatics'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    account_code = db.Column(db.String,
                             db.ForeignKey('acc_accounts.code'), nullable=False)
    status = db.Column(db.String, nullable=False)

    __table_args__ = (UniqueConstraint('code', name='uk_acc_automatics'),)

    def __init__(self, code, name, status, account_code):
        self.code = code
        self.name = name
        self.account_code = account_code
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        automatic_data = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'accountCode': self.account_code,
            'status': self.status
        }
        return automatic_data
