from flask import Blueprint, request, jsonify
from Controllers.EmployeesController import EmployeesController


employeesRoutes = Blueprint('employees', __name__)
employeesController = EmployeesController()


@employeesRoutes.route("/employees", methods=['GET'])
def getInventory():
    data = employeesController.index()
    return jsonify(data)


@employeesRoutes.route("/employees/<id>", methods=['GET'])
def getEmployeesById(id):
    data = employeesController.findEmployees(id)
    return jsonify(data)


@employeesRoutes.route("/employees", methods=['POST'])
def createEmployee():
    dataJson = request.get_json()
    data = employeesController.create(dataJson)
    return jsonify(data)


@employeesRoutes.route("/employees/<id>", methods=['PUT'])
def updateEmployee(id):
    dataJson = request.get_json()
    data = employeesController.update(id, dataJson)
    return jsonify(data)


@employeesRoutes.route("/employees/<id>", methods=['DELETE'])
def deleteEmployee(id):
    data = employeesController.delete(id)
    return jsonify(data)
