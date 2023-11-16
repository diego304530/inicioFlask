from flask import Blueprint, request
from Controllers.ProductsController import ProductsController
from utils.RespHelper import RespHelper

productRoutes = Blueprint('products', __name__)
productsController = ProductsController()


@productRoutes.route("/products", methods=['GET'])
def getProducts():
    data = productsController.index()
    return RespHelper.jsonResp("datos de Producto", [data], 200)


@productRoutes.route("/products", methods=['POST'])
def createProduct():
    dataJson = request.get_json()
    data = productsController.create(dataJson)
    return RespHelper.jsonResp("Producto creado correctamente", [data], 200)
