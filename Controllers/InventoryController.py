from Repositories.InventoryRepository import InventoryRepository
from Models.Inventory import Inventory
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
        currentInventory.idProduct = dataInventory['idProduct']
        currentInventory.quantityInStock = dataInventory['quantityInStock']
        currentInventory.observation = dataInventory['observation']
        return self.inventoryRepository.save(id, currentInventory)

    def delete(self, id):
        return self.inventoryRepository.delete(id)
