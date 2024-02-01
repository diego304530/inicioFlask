from Repositories.ProductsRepository import ProductsRepository
from Models.Products import Products
from Repositories.InventoryRepository import InventoryRepository
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ProductsController():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.productsRepository = ProductsRepository()
        self.inventoryRepository = InventoryRepository()

    def index(self):
        return self.productsRepository.findAll()

    def findProduct(self, id):
        dataProduct = Products(self.productsRepository.findById(id))
        return dataProduct.__dict__

    def create(self, dataProduct):
        newProduct = Products(dataProduct)
        return self.productsRepository.save(newProduct)

    def update(self, id, dataProduct):
        currentProduct = Products(self.productsRepository.findById(id))
        currentProduct.name = dataProduct["name"]
        currentProduct.quantity = dataProduct["quantity"]
        currentProduct.reference = dataProduct['reference']
        currentProduct.price = dataProduct['price']
        return self.productsRepository.save(currentProduct)

    def delete(self, id):
        dataInventory = self.inventoryRepository.findAll()
        for element in dataInventory:
            if (element['product']['_id'] == id):
                print(element['product']['_id'])
                self.inventoryRepository.delete(element['_id'])
        return self.productsRepository.delete(id)
