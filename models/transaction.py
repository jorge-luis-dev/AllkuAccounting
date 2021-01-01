# -*- coding: utf-8 -*-
from app import db


class Transaction(db.Model):
    __tablename__ = 'acc_transactions'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    name = db.Column(db.String, nullable=False)
    editorial = db.Column(db.String, nullable=False)
    published = db.Column(db.String, nullable=False)
    authors = db.relationship('LedgerEntrie',
                              backref='ledgerentrie',
                              lazy='dynamic',
                              cascade="all, delete")

    def __init__(self, name, editorial, published):
        self.name = name
        self.editorial = editorial
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        authors_data = []
        for a in self.authors.all():
            a_data = {}
            a_data['id'] = a.id
            a_data['name'] = a.name
            authors_data.append(a_data)

        book_data = {
            'id': self.id,
            'name': self.name,
            'editorial': self.editorial,
            'published': self.published,
            'authors': authors_data
        }
        return book_data
