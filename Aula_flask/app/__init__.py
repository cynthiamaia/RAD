from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

from app.models.products import Products
with app.app_context(): 
    db.create_all()

from app.view.reso_products import Index,ProductCreate
api.add_resource(Index, '/')
api.add_resource(ProductCreate, '/criar')
'''@app.route("/")
def index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")'''