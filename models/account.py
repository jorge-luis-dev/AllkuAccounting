# -*- coding: utf-8 -*-
import datetime
from app import db
from sqlalchemy import UniqueConstraint, ForeignKey


class Account(db.Model):
    __tablename__ = 'acc_accounts'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey('acc_accounts.id'))
    code = db.Column(db.String(90), nullable=False, unique=True)
    description = db.Column(db.String(180), nullable=False)
    level = db.Column(db.String(90), nullable=False)
    type = db.Column(db.String(90), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=False)
    status = db.Column(db.String(90), nullable=False)
    parent = db.relationship("Account", remote_side=[id])
    UniqueConstraint('code')

    def __init__(self, code='',
                 description='',
                 level='',
                 type='',
                 status='',
                 account_id=None):
        self.code = code
        self.description = description
        self.level = level
        self.type = type
        self.status = status
        self.account_id = account_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        account_data = {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'level': self.level,
            'type': self.type,
            'status': self.status,
            'account_id': self.account_id

        }
        return account_data
