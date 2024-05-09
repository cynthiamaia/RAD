from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_restful import Api 

app = Flask(__name__)
api = Api(app)
#configuração com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud4.db'
db = SQLAlchemy(app)
from app.models.products import Products
with app.app_context():
    db.create_all()

from app.view.reso_products import Index, ProductCreate, ProductUpdate
api.add_resource(Index, '/') #como se fosse a rota, so que com a chamada da api
api.add_resource(ProductCreate, '/criar')
api.add_resource(ProductUpdate, '/atualizar')

'''@app.route("/")
def index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")'''