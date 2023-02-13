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
        If successful, return a string of the inserted_id, None otherwise.
        @Params:
            * doc: dict = Document to be inserted
            * collection: str = Collection to insert document to

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
    
    
    def get_task_by_id(self, id:str) -> dict:
        '''
        Get task by inserted_id.
        @Params:
            * id: string = inserted_id value of Task to find
        @Return: If find is successful, return task in dictionary format. None otherwise.
        '''
        print("- get_task_by_id -")
        doc = self.todo_collection.find_one({'_id':ObjectId(id)})
        doc['_id'] = str(doc['_id'])
        if doc:
            return doc
        else:
            return None

    
    def delete_task_by_id(self, id:str) -> dict:
        '''
        Delete task by inserted_id. 
        @Params:
            * id: string = inserted_id value of Task to be deleted
        @Return: dict with number of deleted tasks
        '''
        print(f"- delete_task({id}) - ")
        # Must convert id to ObjectId
        x = self.todo_collection.delete_one({'_id':ObjectId(id)})
        
        return {'deleted_count':x.deleted_count}


    def update_task_text(self, id:str, new_text:str):
        '''
        Update task description
        @Params:
            * id: string = inserted_id value of Task to be updated
            * new_prio: int = new priority to be set
        @Return: True if update was successful. False otherwise.
        '''
        print("- update_task_by_id() - ")
        result = self.todo_collection.update_one(
            {"_id":ObjectId(id)},
            {"$set":{
                "text": new_text
            }}
            )
        return result.modified_count == 1 
    

    # TODO: refactor update functions into one
    def update_task_priority(self, id:str, new_prio: int):
        '''
        Update task priority
        @Params:
            * id: string = inserted_id value of Task to be updated
            * new_prio: int = new priority to be set
        @Return: True if update was successful. False otherwise.
        '''
        print("- update_task_priority() called - ")
        result = self.todo_collection.update_one(
            {"_id":ObjectId(id)},
            {"$set":{
                "priority": new_prio 
            }}
            )
        return result.modified_count == 1
    
    
    def print_tasks(self):
        for document in self.get_all_tasks():
            print(document)


