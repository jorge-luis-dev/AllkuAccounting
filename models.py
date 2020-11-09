# -*- coding: utf-8 -*-
from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(150), nullable=False)
    published = db.Column(db.String(100), nullable=False)
    authors = db.relationship('Author',
                              backref='book',
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

    
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer,
                        db.ForeignKey('books.id', ondelete='CASCADE'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
