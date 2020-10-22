# -*- coding: utf-8 -*-
from flask_restful import Resource

class Hello(Resource):
    def get(self):
        return {'hello': 'GET'}

    def post(self):
        return {'hello': 'POST'}

