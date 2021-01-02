# -*- coding: utf-8 -*-
from app import db


class AccountView(db.Model):
    # Is recursive view
    __tablename__ = 'v_acc_accounts'
    __table_args__ = {'info': dict(is_view=True)}

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer, nullable=True)


    def __init__(self, code='',
                 name='',
                 location='',
                 type='',
                 status='',
                 account_id=None):
        self.code = code
        self.name = name
        self.location = location
        self.type = type
        self.status = status
        self.account_id = account_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        v_account_data = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'location': self.location,
            'type': self.type,
            'status': self.status,
            'accountId': self.account_id

        }
        return v_account_data
