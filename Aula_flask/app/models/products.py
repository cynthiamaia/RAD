from app import db

class Products(db.Model):
    __tablename__ = 'products'
    __table_args__ = {'sqlite_autoincrement': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)

    def __init__(self, name, price):
        self.name = name
        self.price = price
     
    def save_products(self, name, price):
        try:
            add_banco = Products(name, price)
            print(add_banco)
            db.session.add(add_banco) 
            db.session.commit()
        except Exception as e:
            print(e)

    def update_products(self, id, name, price):
        try:
            db.session.query(Products).filter(Products.id==id).update({"name":name,"price": price})
            db.session.commit() #confirmar e salvar as alterações no banco de dados
        except Exception as e:
            print(e)

