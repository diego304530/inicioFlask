from flask import Blueprint, request, jsonify
from Controllers.ClientsController import ClientsController
from utils.RespHelper import RespHelper
from utils.SendMail import SendMail

clientsRoutes = Blueprint('clients', __name__)
clientsController = ClientsController()
mail = SendMail()


@clientsRoutes.route("/clients", methods=['GET'])
def getClients():
    data = clientsController.index()
    return jsonify(data)


@clientsRoutes.route("/clients/<id>", methods=['GET'])
def getClient(id):
    data = clientsController.findClient(id)
    return jsonify(data)


@clientsRoutes.route("/clients", methods=['POST'])
def createClient():
    dataJson = request.get_json()
    data = clientsController.create(dataJson)
    return jsonify(data)


@clientsRoutes.route("/clients/<id>", methods=['PUT'])
def updateClient(id):
    dataJson = request.get_json()
    data = clientsController.update(id, dataJson)
    return jsonify(data)


@clientsRoutes.route("/clients/<id>", methods=['DELETE'])
def deleteClient(id):
    data = clientsController.delete(id)
    return jsonify(data)


@clientsRoutes.route("/sendMail", methods=['POST'])
def sendEmail():
    dataJson = request.get_json()
    data = mail.formatMessage(dataJson)
    return jsonify(data)
