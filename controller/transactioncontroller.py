# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from flask import jsonify, request
from app import db
from models.ledgerentrie import LedgerEntrie
from models.transaction import Transaction
from models.document import Document

parser = reqparse.RequestParser()


class TransactionListController(Resource):

    def get(self):
        try:
            transactions = Transaction.query.all()
            return jsonify([b.serialize() for b in transactions])
        except Exception as e:
            return str(e), 404

    def post(self):
        data = request.get_json()
        print(data)
        try:
            name = data['name']
            editorial = data['editorial']
            published = data['published']
            transaction = Transaction(name=name, editorial=editorial, published=published)

            for a in data['authors']:
                transaction.authors.append(LedgerEntrie(name=a['name']))
                print(a)

            db.session.add(transaction)
            db.session.commit()
            return "Book added. transaction id={}".format(transaction.id), 201
        except Exception as e:
            return str(e), 400


class TransactionController(Resource):

    def get(self, id_transaction):
        try:
            transaction = Transaction.query.filter_by(id=id_transaction).first()
            if transaction is None:
                return None, 404
            return jsonify(transaction.serialize())
        except Exception as e:
            return str(e), 404

    def put(self, id_transaction):
        parser.add_argument('name')
        parser.add_argument('author')
        parser.add_argument('published')
        args = parser.parse_args()
        name = args['name']
        author = args['author']
        published = args['published']
        try:
            transaction = Transaction.query.filter_by(id=id_transaction).first()
            if transaction is None:
                return None, 204
            transaction.name = name
            transaction.author = author
            transaction.published = published
            db.session.commit()
            return jsonify(transaction.serialize())
        except Exception as e:
            return str(e), 409

    def delete(self, id_transaction):
        try:
            transaction = Transaction.query.filter_by(id=id_transaction).first()
            if transaction is None:
                return None, 404
            db.session.delete(transaction)
            db.session.commit()
            return jsonify(transaction.serialize())
        except Exception as e:
            return str(e), 404
