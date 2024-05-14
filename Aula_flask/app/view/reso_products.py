from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.products import Products

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)

#para atualizar
argumentos_update = reqparse.RequestParser() #definir os argumentos da solicitação HTTP
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos_update.add_argument('price', type=float)


class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Products.save_products(self, datas['name'], datas['price'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500

class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Products.update_products(self, datas['id'], 
            datas['name'],
            datas['price'],
            )
            return {"message": 'Products update successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500



