# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from models import Book


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add")
def add_book():
    name = request.args.get('name')
    author = request.args.get('author')
    published = request.args.get('published')
    try:
        book = Book(name=name, author=author, published=published)
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
        return (str(e))


@app.route("/getall")
def get_all():
    try:
        books = Book.query.all()
        return jsonify([e.serialize() for e in books])
    except Exception as e:
        return (str(e))


@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book = Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
        return (str(e))



if __name__ == '__main__':
    app.run()
