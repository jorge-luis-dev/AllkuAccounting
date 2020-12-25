# -*- coding: utf-8 -*-
from app import db
from sqlalchemy import UniqueConstraint


class Document(db.Model):
    __tablename__ = 'adm_documents'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    code = db.Column(db.String(90), nullable=False, unique=True)
    description = db.Column(db.String(180), nullable=False)
    operator = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(90), nullable=False)
    UniqueConstraint('code')

    def __init__(self, code='',
                 description='',
                 operator=0,
                 status=''):
        self.code = code
        self.description = description
        self.operator = operator
        self.status = status

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        document_data = {
            'id': self.id,
            'code': self.code,
            'description': self.description,
            'operator': self.operator,
            'status': self.status
        }
        return document_data
