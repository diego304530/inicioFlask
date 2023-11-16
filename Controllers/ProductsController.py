from Repositories.ProductsRepository import ProductsRepository
from Models.Product import Product
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

    def index(self):
        return self.productsRepository.findAll()

    def findProduct(self, id):
        dataProduct = Product(self.productsRepository.findById(id))
        return dataProduct.__dict__

    def create(self, dataProduct):
        newProduct = Product(dataProduct)
        return self.productsRepository.save(newProduct)

    def update(self, id, dataProduct):
        currentProduct = Product(self.productsRepository.findById(id))
        currentProduct.description = dataProduct["description"]
        currentProduct.unitValue = dataProduct["unitValue"]
        currentProduct.quantityAvailable = dataProduct['quantityAvailable']
        currentProduct.unit = dataProduct['unit']
        return self.productsRepository.save(id, currentProduct)

    def delete(self, id):
        return self.productsRepository.delete(id)
