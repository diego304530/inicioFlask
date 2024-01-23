from Repositories.InventoryRepository import InventoryRepository
from Repositories.ProductsRepository import ProductsRepository
from Repositories.EmployeesRepository import EmployeesRepository
from Models.Inventory import Inventory
from Models.Products import Products
from Models.Employees import Employees
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class InventoryController():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.inventoryRepository = InventoryRepository()
        self.productsRepository = ProductsRepository()
        self.employeesRepository = EmployeesRepository()

    def index(self):
        return self.inventoryRepository.findAll()

    def findInventory(self, id):
        dataInventory = Inventory(self.inventoryRepository.findById(id))
        return dataInventory.__dict__

    def create(self, dataInventory):
        newInventory = Inventory(dataInventory)
        return self.inventoryRepository.save(newInventory)

    def update(self, id, dataInventory):
        currentInventory = Inventory(self.inventoryRepository.findById(id))
        currentInventory.date = dataInventory["date"]
        currentInventory.quentity = dataInventory["quantity"]
        currentInventory.quantityInStock = dataInventory['quantityInStock']
        currentInventory.observation = dataInventory['observation']
        if "idProduct" in dataInventory:
            product = self.productsRepository.findById(
                dataInventory["idProduct"])
            currentInventory.product = product
        if "idEmployee" in dataInventory:
            employee = self.employeesRepository.findById(
                dataInventory["idEmployee"])
            currentInventory.employee = employee

        return self.inventoryRepository.save(currentInventory)

    def delete(self, id):
        return self.inventoryRepository.delete(id)

    # def findInventoryByYear(self, anio):
    #     query = {}
    #     return self.inventoryRepository.query(query)

    # asignacion de un producto a un inventario
    def setProductToInventory(self, idInventory, idProduct):
        dataInventory = Inventory(
            self.inventoryRepository.findById(idInventory))
        dataProduct = Products(self.productsRepository.findById(idProduct))
        dataInventory.product = dataProduct
        return self.inventoryRepository.save(dataInventory)

    def setEmployeeToInventory(self, idInventory, idEmployee):
        dataInventory = Inventory(
            self.inventoryRepository.findById(idInventory))
        dataEmployee = Employees(self.employeesRepository.findById(idEmployee))
        dataInventory.employee = dataEmployee
        return self.inventoryRepository.save(dataInventory)
