from flask import Blueprint, request
from Controllers.InventoryController import InventoryController
from utils.RespHelper import RespHelper

inventoryRoutes = Blueprint('inventory', __name__)
inventoryController = InventoryController()


@inventoryRoutes.route("/inventory", methods=['GET'])
def getInventory():
    data = inventoryController.index()
    return RespHelper.jsonResp("datos de Inventario", [data], 200)


@inventoryRoutes.route("/inventory/<id>", methods=['GET'])
def getInventoryById(id):
    data = inventoryController.findInventory(id)
    return RespHelper.jsonResp("datos de Inventario", [data], 200)


@inventoryRoutes.route("/inventory", methods=['POST'])
def createInventory():
    dataJson = request.get_json()
    data = inventoryController.create(dataJson)
    return RespHelper.jsonResp("Inventario creado correctamente", [data], 200)


@inventoryRoutes.route("/inventory/<id>", methods=['PUT'])
def updateInventory(id):
    dataJson = request.get_json()
    data = inventoryController.update(id, dataJson)
    return RespHelper.jsonResp("Inventario actualizado correctamente", [data], 200)


@inventoryRoutes.route("/inventory/<id>", methods=['DELETE'])
def deleteInventory(id):
    dataJson = request.get_json()
    data = inventoryController.delete(id)
    return RespHelper.jsonResp("Inventario actualizado correctamente", [data], 200)
