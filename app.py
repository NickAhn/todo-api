from flask import Flask, render_template, request, jsonify
import database
from task import Task
from pprint import pprint

app = Flask(__name__)
db = database.Database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/add", methods=['POST'])
def add():
    '''
    POST request to add new Task to database
    @Body params:
        *   'text': Task description
        *   'priority': Priority of the task (1-4)
    '''
    try:
        body = request.get_json()
        priority = body['priority'] if 'priority' in body else None

        newTask = Task(text=body['text'], priority=priority)
        inserted_id = db.insert_doc(newTask.to_json())
        return jsonify({'status:':'ok', 'inserted_id':inserted_id, 'task':newTask.to_json()})
    except Exception as e:
        return jsonify({"status":"error", "error_message":str(e)})


@app.route("/api/get-all-tasks", methods=['GET'])
def get_all_tasks():
    '''
    GET request to get all tasks in database
    '''
    return db.get_all_tasks()


@app.route('/api/delete', methods=['DELETE'])
def delete_task_by_id():
    '''
    DEL request to delete task by id
    '''
    body = request.get_json()
    try:
        x = db.delete_task_by_id(body['id'])
        print(x)
        return jsonify(x)
    except Exception as e:
        return jsonify({"status":"error", "error_message":e})


@app.route("/api/test", methods=['GET', 'POST'])
def test():
    '''
    Endpoint just to test GET and POST requests
    '''
    if request.method == 'GET':
        return jsonify({"response":"Get request called"})
    if request.method == 'POST':
        req = request.json
        name = req['name']
        return jsonify({'response':'Hi ' + name})


if __name__ == "__main__":
    app.run(debug=True)