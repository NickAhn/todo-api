# TODO webapp and API
A todo list web application and API written with Python, Flask, and MongoDB 

***(work in progress)***

## TODO CLI
A Command-line interface version of the todo list is being developed. The app is being developed with [Go](https://go.dev/) and Cobra, and it performs CRUD operations through the API in this repository.

Link to project: [**todo-cli**](https://github.com/NickAhn/todo-cli)

# API Documentation
## Table of Contents

### GET
* [Get Task by id](#get-task-by-id)
* [Get All Tasks](#get-all-tasks)

### POST
* [Add Task](#add-task)

### PUT
* 

### DELETE
* [Delete task by id](#delete-task)
<hr>

[//]: ---------------------------------------------

## Get Task By Id
> Get Task by its inserted_id

### Endpoint
* ```/api/get-task-by-id```
### Method
* **GET**
### Responses
**Successful Response**
* Returns a json with the Task metadata
* Content:
    ```
    {
        'text': string,
        'priority': int,
        'completed': bool,
        '_id': string
    }
    ```
**Error Response**
* Content:
    ```
    {
        'status': 'error',
        'error_message': string
    }
    ```
[(Back to top)](#table-of-contents)

## Get All Tasks
> Get list of all tasks in database
### Endpoint
* ```/api/get-all-tasks```

### Method
* **GET**

### Responses
**Successful Response**
* Content:

    ```
    [
        {
            'text': string,
            'priority': int,
            'completed': bool
            '_id': string
        }
        (...)
    ]
    ```

[(Back to top)](#table-of-contents)


## Add Task
> Add a task to todo list database
### Endpoint
* ```/api/add```

### Method
* **POST**
### Params
application/json
* **text** *string*

    Task description

* **priority** *int* (Optional)

    Task Priority (1-4). If none provided, priority is set to 4 by default.

### Responses
**Success Response**
* Code: 200
* Content:
    ```
    {
        'status': 'ok',
        'inserted_id': string,
        'task': {
            'text': string,
            'priority': int,
            'completed': bool
            '_id': string
        }
    }
    ```

**error response**
* content:
    ```
    {
    'status': 'error',
    'error_message': string
    }
    ```

[(Back to top)](#table-of-contents)


## Delete Task
> Delete Task by *inserted_id*
### Endpoint
* ```/api/delete```

### Method
* **DELETE**

### Params
application/json
* **id** str

    inserted_id of task to be deleted

### Responses
**Successful Response**:
* Deletes task from database and returns a json with deleted count.
* Content:
    ```
    {
        'status': 'ok',
        'deleted_count': int
    }
    ```

**error response**
* Content:
    ```
    {
    'status': 'error',
    'error_message': string
    }
    ```

[(Back to top)](#table-of-contents)