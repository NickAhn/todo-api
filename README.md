# TODO webapp
A todo list web application and API written with Python, Flask, and MongoDB 

***(work in progress)***

# API Documentation
## Add Task
Add a task to todo list database
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

**Error Response**
* Content:
    ```
    {
    'status': 'error',
    'error_message': string
    }
    ```

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

**Error Response**
* Content:
    ```
    {
        'status': 'error',
        'error_message': string
    }
    ```
