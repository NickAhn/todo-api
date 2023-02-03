from pymongo import MongoClient
from pprint import pprint
from cred import pwd

def get_db():
    '''
    Create MongoClient instance
    '''
    connection_string = f"mongodb+srv://nickel:{pwd}@todo-db.hnwi9a3.mongodb.net/?retryWrites=true&w=majority"
    try:
        client = MongoClient(connection_string)
    except Exception as e:
        print("Error:", e)
        return

    return client

def insert_doc(doc, collection):
    '''
    Insert document to collection. If successful, return inserted_id. None otherwise
    @Param:
        * doc: Document to be inserted
        * collection: Collection to insert documnet to
    @Return: inserted_id
    '''
    inserted_id = collection.insert_one(doc).inserted_id
    if inserted_id:
        print(inserted_id, type(inserted_id))
        print(db.list_collection_names())
        return inserted_id
    return

client = get_db()
print("- Getting todo-db - ")
db = client['todo-db']

print("- Getting nickel-todo collection -")
collection= db['nickel-todo']




