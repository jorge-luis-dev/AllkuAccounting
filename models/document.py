# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import UniqueConstraint


class Document(db.Model):
    # Code of documents example: ENI, SAI, DGD, etc
    __tablename__ = 'adm_documents'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    operator = db.Column(db.Integer, nullable=False)
    module = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    transactions = db.relationship('Transaction',
                                     backref='document')
    __table_args__ = (UniqueConstraint('code', name='uk_adm_documents'),)

    def __init__(self, code='',
                 name='',
                 operator=0,
                 module='',
                 status=''):
        self.code = code
        self.name = name
        self.operator = operator
        self.module = module
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        document_data = {
            'id': self.id,
            'code': self.code,
            'name': self.name,
            'operator': self.operator,
            'module': self.module,
            'status': self.status
        }
        return document_data
