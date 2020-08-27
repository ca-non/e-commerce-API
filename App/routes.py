from flask_restful import Resource
from flask import request, jsonify
from App.models import Product, Admin, product_schema, products_schema, admin_schema
from flask_httpauth import HTTPBasicAuth
from App import db, api

auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    user = Admin.query.filter_by(username=username).first()

    if username and password:
        return user.password == password
    return False
    
class ProductPara(Resource):
    def get(self, name):
        product = Product.query.filter_by(name=name).first()
        return product_schema.jsonify(product)

    @auth.login_required
    def put(self, name):
        product = Product.query.filter_by(name=name).first()

        product.name = request.json['name']
        product.description = request.json['description']
        product.price = request.json['price']
        product.quantity = request.json['quantity']

        db.session.commit()

        return product_schema.jsonify(product)

    @auth.login_required
    def delete(self,name):
        product = Product.query.filter_by(name=name).first()

        db.session.delete(product)
        db.session.commit()

        return product.name + ' deleted!'


class ProductNoPara(Resource):
    @auth.login_required
    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

        new_product = Product(name, description, price, quantity)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)


    def get(self):
        products = Product.query.all()
        return products_schema.jsonify(products)



# Routes
api.add_resource(ProductPara, '/api/v1/product/<string:name>')
api.add_resource(ProductNoPara, '/api/v1/product')
