# -*- coding: utf-8 -*-
import datetime
from app import db
from sqlalchemy import UniqueConstraint, ForeignKey


class Account(db.Model):
    # Is used to save accounting accounts
    __tablename__ = 'acc_accounts'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    status = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer, ForeignKey('acc_accounts.id'))
    parent = db.relationship("Account", remote_side=[id])
    UniqueConstraint('code')

    def __init__(self, code='',
                 name='',
                 type='',
                 status='',
                 account_id=None):
        self.code = code
        self.name = name
        self.type = type
        self.status = status
        self.account_id = account_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        account_data = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'type': self.type,
            'status': self.status,
            'accountId': self.account_id

        }
        return account_data
