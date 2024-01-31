from flask import Blueprint, request, jsonify
from Controllers.ProductsController import ProductsController
from utils.RespHelper import RespHelper

productRoutes = Blueprint('products', __name__)
productsController = ProductsController()


@productRoutes.route("/products", methods=['GET'])
def getProducts():
    data = productsController.index()
    return jsonify(data)


@productRoutes.route("/products/<id>", methods=['GET'])
def getProduct(id):
    data = productsController.findProduct(id)
    return jsonify(data)


@productRoutes.route("/products", methods=['POST'])
def createProduct():
    dataJson = request.get_json()
    data = productsController.create(dataJson)
    return jsonify(data)


@productRoutes.route("/products/<id>", methods=['PUT'])
def updateProduct(id):
    dataJson = request.get_json()
    data = productsController.update(id, dataJson)
    return jsonify(data)


@productRoutes.route("/products/<id>", methods=['DELETE'])
def deleteProduct(id):
    data = productsController.delete(id)
    return jsonify(data)
