from pymongo import MongoClient
from pprint import pprint
from cred import pwd
import json
from bson import BSON, ObjectId

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
        docs = self.todo_collection.find({})
        for doc in docs:
            doc['_id'] = str(doc['_id'])
            tasks.append(doc)

        return tasks
    
    def delete_task_by_id(self, id:str):
        '''
        Delete task by id. 
        @Params:
            * id:string = inserted_id value of Task to be deleted
        @Return: dict with number of deleted tasks
        '''
        print(f"- delete_task({id}) - ")
        # Must convert id to ObjectId
        x = self.todo_collection.delete_one({'_id':ObjectId(id)})
        
        return {'deleted_count':x.deleted_count}






    def print_tasks(self):
        for document in self.get_all_tasks():
            print(document)


