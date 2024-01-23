from Repositories.EmployeesRepository import EmployeesRepository
from Models.Employees import Employees
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class EmployeesController():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.employeesRepository = EmployeesRepository()

    def index(self):
        return self.employeesRepository.findAll()

    def findEmployees(self, id):
        dataEmployees = Employees(self.employeesRepository.findById(id))
        return dataEmployees.__dict__

    def create(self, dataEmployees):
        newEmployee = Employees(dataEmployees)
        return self.employeesRepository.save(newEmployee)

    def update(self, id, dataEmployee):
        currentEmployee = Employees(self.employeesRepository.findById(id))
        currentEmployee.name = dataEmployee["name"]
        currentEmployee.lastName = dataEmployee["lastName"]
        currentEmployee.address = dataEmployee['address']
        currentEmployee.email = dataEmployee['email']
        return self.employeesRepository.save(currentEmployee)

    def delete(self, id):
        return self.employeesRepository.delete(id)
