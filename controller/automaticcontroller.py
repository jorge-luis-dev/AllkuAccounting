# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.automatic import Automatic


class AutomaticListController(Resource):
    # Return all automatics parameters
    def get(self):
        try:
            automatic = Automatic.query.order_by(
                Automatic.code.asc()
                ).all()
            return jsonify([b.serialize() for b in automatic])
        except Exception as e:
            return str(e), 404
