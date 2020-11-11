from flask import Blueprint

models = Blueprint('models', __name__)

from . import book, author
