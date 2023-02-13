from flask import Flask, render_template, request, jsonify
import database
from task import Task
from pprint import pprint

app = Flask(__name__)
db = database.Database()


@app.route("/")
def home():
    return render_template("index.html")

# TODO: change names of routes to follow REST practices
@app.route("/api/tasks", methods=['POST'])
def add():
    '''
    POST request to add new Task to database
    @Body params:
        *   'text': Task description
        *   'priority': Priority of the task (1-4)
    '''
    print("- ADD route called - ")
    try:
        body = request.get_json()
        priority = body['priority'] if 'priority' in body else None

        newTask = Task(text=body['text'], priority=priority)
        inserted_id = db.insert_doc(newTask.to_json())
        return jsonify({'status:':'ok', 'inserted_id':inserted_id, 'task':newTask.to_json()})
    except Exception as e:
        return jsonify({"status":"error", "error_message":str(e)})


@app.route("/api/tasks", methods=['GET'])
def get_all_tasks():
    '''
    GET request to get all tasks in database
    '''
    return db.get_all_tasks()


@app.route("/api/tasks/<string:id>", methods=['GET'])
def get_task_by_id(id):
    '''
    GET request to get task by inserted_id
    @Query params:
        * id: string = inserted_id (Required)
    '''
    print("- get_task_by_id() called - ")
    try:
        print(
            'app route'
        )
        # inserted_id = request.args['id']
        # print('inserted_id', inserted_id)
        # doc = db.get_task_by_id(inserted_id)
        print('id', id)
        doc = db.get_task_by_id(id)
        return jsonify(doc)

    except Exception as e:
        return jsonify({
            'status':'error',
            'error_message':str(e)
        })
        
@app.route("/api/tasks/<string:id>", methods=['PUT'])
def update_task_text(id):
    '''
    PUT request to update task description
    @Params:
        * id: string = inserted_id
    '''
    body = request.get_json()
    try:
        success = db.update_task_text(id=id, new_text=body['new_text'])
        msg = ''
        if not success:
            msg = 'Task has not been updated. Check if inserted_id provided is valid'
        return jsonify({
            'status':'ok',
            'updated': str(success)
        })
        
    except KeyError as e:
        return jsonify({
            'status':'error',
            'error_message': 'Incorrect/missing key. ' + str(e)
        })


@app.route("/api/tasks/<string:id>", methods=['DELETE'])
def delete_task_by_id(id):
    '''
    DEL request to delete task by id
    '''
    # body = request.get_json()
    try:
        # x = db.delete_task_by_id(body['id'])
        x = db.delete_task_by_id(id)
        print(x)
        return jsonify(x)
    except Exception as e:
        return jsonify({"status":"error", "error_message":e})


@app.route("/api/test/<string:id>", methods=['GET', 'POST'])
def test(id):
    '''
    Endpoint just to test GET and POST requests
    '''
    if request.method == 'GET':
        return jsonify({"response":"Get request called"})
    if request.method == 'POST':
        req = request.json
        name = req['name']
        return jsonify({'response':'Hi ' + id})


if __name__ == "__main__":
    app.run(debug=True)