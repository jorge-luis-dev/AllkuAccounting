# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.automatic import Automatic


class AutomaticSimpleController(Resource):
    # Return all automatics parameters
    def get(self):
        try:
            automatic = Automatic.query.order_by(
                Automatic.code.asc()
            ).all()
            return jsonify([b.serialize() for b in automatic])
        except Exception as e:
            return str(e), 404

    # Insert new automatic parameter
    def post(self):
        data = request.get_json()
        print(data)
        try:
            code = data['code']
            name = data['name']
            account_code = data['accountCode']
            status = data['status']

            automatic = Automatic(code, name, status, account_code)

            db.session.add(automatic)
            db.session.commit()
            return "Automatic added. Id={}".format(automatic.id), 201
        except Exception as e:
            return str(e), 400


class AutomaticController(Resource):
    # Return automatic by id
    def get(self, id_automatic):
        try:
            automatic = Automatic.query.filter_by(id=id_automatic).first()
            if automatic is None:
                return None, 404

            return jsonify(automatic.serialize())
        except Exception as e:
            return str(e), 404

    # Update automatic by id
    def put(self, id_automatic):
        data = request.get_json()
        print(data)
        try:
            code = data['code']
            name = data['name']
            account_code = data['accountCode']
            status = data['status']

            automatic = Automatic.query.filter_by(id=id_automatic).first()
            if automatic is None:
                return None, 204

            automatic.code = code
            automatic.name = name
            automatic.account_code = account_code
            automatic.status = status
            db.session.commit()
            return jsonify(automatic.serialize())
        except Exception as e:
            return str(e), 409

    # Delete automatic by id
    def delete(self, id_automatic):
        try:
            automatic = Automatic.query.filter_by(id=id_automatic).first()
            if automatic is None:
                return None, 404

            db.session.delete(automatic)
            db.session.commit()
            return jsonify(automatic.serialize())
        except Exception as e:
            return str(e), 404


class AutomaticCodeController(Resource):
    # Return automatic by code
    def get(self, code):
        try:
            account = Automatic.query.filter_by(code=code).first()
            if account is None:
                return None, 404

            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404
