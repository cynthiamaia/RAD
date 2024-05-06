from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.products import Products
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str,help= 'Name of the product')
argumentos.add_argument('price', type=float, help= 'Price of the product')

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Products.save_products(self, datas['name'], datas['price'])
            return {"message": 'Products create successfully!'}, 201
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500