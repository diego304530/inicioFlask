from Repositories.ClientsRepository import ClientsRepository
from Models.Clients import Clients
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ClientsController():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.clientsRepository = ClientsRepository()

    def index(self):
        return self.clientsRepository.findAll()

    def findClient(self, id):
        dataClients = Clients(self.clientsRepository.findById(id))
        return dataClients.__dict__

    def create(self, dataClients):
        newClient = Clients(dataClients)
        return self.clientsRepository.save(newClient)

    def update(self, id, dataClients):
        currentClients = Clients(self.clientsRepository.findById(id))
        currentClients.name = dataClients["name"]
        currentClients.lastName = dataClients["lastName"]
        currentClients.address = dataClients['address']
        currentClients.email = dataClients['email']
        currentClients.birthdayDate = dataClients['birthdayDate']
        return self.clientsRepository.save(currentClients)

    def delete(self, id):
        return self.clientsRepository.delete(id)
