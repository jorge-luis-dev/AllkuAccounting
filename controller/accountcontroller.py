# -*- coding: utf-8 -*-
from flask_restful import Resource
from flask import jsonify, request
from app import db
from models.account import Account
from models.account_view import AccountView


class AccountSimpleController(Resource):
    # Return all accounts
    def get(self):
        try:
            account = AccountView.query.order_by(
                AccountView.code.asc()
                ).all()
            return jsonify([b.serialize() for b in account])
        except Exception as e:
            return str(e), 404

    # Insert new account
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
            return "Account added. Id={}".format(account.id), 201
        except Exception as e:
            return str(e), 400


class AccountController(Resource):
    # Return account by id
    def get(self, id_account):
        try:
            account = AccountView.query.filter_by(id=id_account).first()
            if account is None:
                return None, 404
            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404

    # Update account by id, only update: name, type and status
    def put(self, id_account):
        data = request.get_json()
        print(data)
        try:
            name = data['name']
            type = data['type']
            status = data['status']

            account = Account.query.filter_by(id=id_account).first()
            if account is None:
                return None, 204

            account.name = name
            account.type = type
            account.status = status
            db.session.commit()
            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 409

    # Delete account by id
    def delete(self, id_account):
        try:
            account = Account.query.filter_by(id=id_account).first()
            if account is None:
                return None, 404

            db.session.delete(account)
            db.session.commit()
            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404


class AccountCodeController(Resource):
    # Return account by code
    def get(self, code):
        try:
            account = AccountView.query.filter_by(code=code).first()
            if account is None:
                return None, 404

            return jsonify(account.serialize())
        except Exception as e:
            return str(e), 404
