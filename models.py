# -*- coding: utf-8 -*-
from app import db
from flask import jsonify


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(150), nullable=False)
    published = db.Column(db.String(100), nullable=False)
    authors = db.relationship('Author', backref='book', lazy='dynamic')

    def __init__(self, name, editorial, published):
        self.name = name
        self.editorial = author
        self.published = published

    def to_json(self):
        
        res_data = []
        for a in self.authors.all():
            tmp = {}
            tmp['id']=a.id
            tmp['name']=a.name
            res_data.append(tmp)
            print(a.id)
            print(a.name)


        json_book = {
            'id': self.id,
            'name': self.name,
            'editorial': self.editorial,
            'published': self.published,
            'authors': res_data
        }
        return json_book

    # def __repr__(self):
    #     return '<id {}>'.format(self.id)

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'author': self.author,
    #         'published': self.published
    #     }


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }