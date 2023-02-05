from pymongo import MongoClient
from pprint import pprint
from cred import pwd
import json
from bson import BSON

class Database:
    def __init__(self) -> None:
        '''
        Create MongoClient instance
        '''
        connection_string = f"mongodb+srv://nickel:{pwd}@todo-db.hnwi9a3.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)

        self.db = client['todo-db']
        self.todo_collection = self.db['nickel-todo']

    def insert_doc(self, doc) -> str:
        '''
        Insert document to collection.
        If successful, return a bson object of the inserted_id, None otherwise.
        @Params:
            * doc:BSON = Document to be inserted
            * collection:str = Collection to insert documnet to

        @Return: inserted_id
        '''
        print("- insert_doc() - ")
        inserted_id = self.todo_collection.insert_one(doc).inserted_id
        if inserted_id:
            return str(inserted_id)
        return

    def get_all_tasks(self) -> list:
        '''
        Get all documents in todo_collection
        @Return: list of Task dictionaries
        '''
        print("- getting tasks - ")
        tasks = []
        docs = self.todo_collection.find({}, projection={'_id': False})
        for doc in docs:
            tasks.append(doc)

        return tasks

    def print_tasks(self):
        for document in self.get_all_tasks():
            print(document)


