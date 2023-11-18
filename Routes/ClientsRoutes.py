from flask import Blueprint, request
from Controllers.ClientsController import ClientsController
from utils.RespHelper import RespHelper

clientsRoutes = Blueprint('clients', __name__)
clientsController = ClientsController()


@clientsRoutes.route("/clients", methods=['GET'])
def getClients():
    data = clientsController.index()
    return RespHelper.jsonResp("datos de Clientes", [data], 200)

    @clientsRoutes.route("/clients/<id>", methods=['GET'])
def getClient(id):
    data = clientsController.findClient(id)
    return RespHelper.jsonResp("datos del Cliente", [data], 200)


@clientsRoutes.route("/clients", methods=['POST'])
def createClient():
    dataJson = request.get_json()
    data = clientsController.create(dataJson)
    return RespHelper.jsonResp("Cliente creado correctamente", [data], 200)


@clientsRoutes.route("/clients/<id>", methods=['PUT'])
def updateClient(id):
    dataJson = request.get_json()
    data = clientsController.update(id, dataJson)
    return RespHelper.jsonResp("Cliente actualizado correctamente", [data], 200)


@clientsRoutes.route("/clients/<id>", methods=['DELETE'])
def deleteProduct(id):
    dataJson = request.get_json()
    data = clientsController.delete(id)
    return RespHelper.jsonResp("Producto actualizado correctamente", [data], 200)
