# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from flask import jsonify, request
from app import db
from models.author import Author
from models.book import Book

parser = reqparse.RequestParser()


class BookListApi(Resource):

    def get(self):
        try:
            books = Book.query.all()
            return jsonify([b.serialize() for b in books])
        except Exception as e:
            return str(e), 404

    def post(self):
        data = request.get_json()
        print(data)
        try:
            name = data['name']
            editorial = data['editorial']
            published = data['published']
            book = Book(name=name, editorial=editorial, published=published)

            for a in data['authors']:
                book.authors.append(Author(name=a['name']))
                print(a)

            db.session.add(book)
            db.session.commit()
            return "Book added. book id={}".format(book.id), 201
        except Exception as e:
            return str(e), 400


class BookApi(Resource):

    def get(self, id_book):
        try:
            book = Book.query.filter_by(id=id_book).first()
            if book is None:
                return None, 404
            return jsonify(book.serialize())
        except Exception as e:
            return str(e), 404

    def put(self, id_book):
        parser.add_argument('name')
        parser.add_argument('author')
        parser.add_argument('published')
        args = parser.parse_args()
        name = args['name']
        author = args['author']
        published = args['published']
        try:
            book = Book.query.filter_by(id=id_book).first()
            if book is None:
                return None, 204
            book.name = name
            book.author = author
            book.published = published
            db.session.commit()
            return jsonify(book.serialize())
        except Exception as e:
            return str(e), 409

    def delete(self, id_book):
        try:
            book = Book.query.filter_by(id=id_book).first()
            if book is None:
                return None, 404
            db.session.delete(book)
            db.session.commit()
            return jsonify(book.serialize())
        except Exception as e:
            return str(e), 404
