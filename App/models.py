from App import db, ma

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password

#schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'price', 'quantity')


class AdminSchema(ma.Schema):
    class Meta:
        fields = ('password',)


#Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
admin_schema = AdminSchema()
