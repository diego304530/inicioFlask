from flask import Blueprint, request, jsonify
from Controllers.InventoryController import InventoryController
from utils.RespHelper import RespHelper

inventoryRoutes = Blueprint('inventory', __name__)
inventoryController = InventoryController()


@inventoryRoutes.route("/inventory", methods=['GET'])
def getInventory():
    data = inventoryController.index()
    return jsonify(data)


@inventoryRoutes.route("/inventory/<id>", methods=['GET'])
def getInventoryById(id):
    data = inventoryController.findInventory(id)
    return jsonify(data)


@inventoryRoutes.route("/inventory", methods=['POST'])
def createInventory():
    dataJson = request.get_json()
    data = inventoryController.create(dataJson)
    return jsonify(data), 201


@inventoryRoutes.route("/inventory/<id>", methods=['PUT'])
def updateInventory(id):
    dataJson = request.get_json()
    data = inventoryController.update(id, dataJson)
    return jsonify(data)


@inventoryRoutes.route("/inventory/<id>", methods=['DELETE'])
def deleteInventory(id):
    dataJson = request.get_json()
    data = inventoryController.delete(id)
    return jsonify(data)


@inventoryRoutes.route("/inventory/<id>/product/<idProduct>", methods=['PUT'])
def setProductToInventory(id, idProduct):
    data = inventoryController.setProductToInventory(id, idProduct)
    return jsonify(data)


@inventoryRoutes.route("/inventory/<id>/employee/<idEmployee>", methods=['PUT'])
def setEmployeeToInventory(id, idEmployee):
    data = inventoryController.setEmployeeToInventory(id, idEmployee)
    return jsonify(data)
