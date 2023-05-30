from pymongo import MongoClient
from pymongo.server_api import ServerApi


class ClientFactory:

    def get_client(self):
        return MongoClient(
            'mongodb+srv://felipemalaguti:Ma1a6uti@cluster0.eyd5olo.mongodb.net/?retryWrites=true&w=majority', 
            server_api=ServerApi('1'))