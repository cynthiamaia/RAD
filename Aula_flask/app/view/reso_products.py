from flask import jsonify
from flask_restful import Resource
from app.models.products import Products

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")