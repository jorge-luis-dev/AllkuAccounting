# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.account import Account


class AccountListController(Resource):
    def get(self):
        try:
            account = Account.query.all()
            return jsonify([b.serialize() for b in account])
        except Exception as e:
            return str(e), 404

    def post(self):
        data = request.get_json()
        print(data)
        try:
            code = data['code']
            name = data['name']
            type = data['type']
            status = data['status']

            if code.find(".") > 0:
                # Search father account to foreign key
                code_father = code[0:code.rfind(".")]
                account = Account.query.filter_by(code=code_father).first()
                print("Father account: ")
                print(account)
                if account is None:
                    print("No existe la cuenta padre")
                    return None, 400
                else:
                    account_id = account.id
                    account = Account(code=code,
                                      name=name,
                                      type=type,
                                      status=status,
                                      account_id=account_id)
            else:
                account = Account(code=code,
                                  name=name,
                                  type=type,
                                  status=status)

            db.session.add(account)
            db.session.commit()
            return "Account added. account id={}".format(account.id), 201
        except Exception as e:
            return str(e), 400


class AccountController(Resource):
    def get(self, id_account):
        try:
            account = Account.query.filter_by(id=id_account).first()
            if account is None:
                return None, 404
            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404


class AccountCodeController(Resource):
    def get(self, code):
        try:
            account = Account.query.filter_by(code=code).first()
            if account is None:
                return None, 404
            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404
