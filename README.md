# REST API for Teams and People Management

This repository contains a REST API implementation for managing teams and people associated with those teams. The API provides CRUD (create, read, update, delete) endpoints for handling teams and people entities. Below are the details of the API:

## Team Object
A team object has the following attribute:
- `name`: The name of the team.

## Person Object
A person object has the following attributes:
- `name`: First name of the person.
- `surname`: Last name of the person.
- `email`: Email address of the person.

## Testing the API

To test this API, you can use the interactive Swagger documentation. To do this, click on the following link:

[Swagger Documentation and API Testing](http://127.0.0.1:8000/docs#/)

Swagger provides a convenient interface to make requests to the API. You can check available endpoints, see what parameters they expect, and even try out real requests.


## API Endpoints

### Create a User
Endpoint: `http://127.0.0.1:8000/user/create/`  
Method: `POST`  
Request Body:
```json
{
    "name": str,
    "surname": str,
    "email": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```

### Get User information
Endpoint: `http://127.0.0.1:8000/user/info/`  
Method: `GET`  
Request Body:
```json
{
    "email": str
}
```

Response:
```json
{
    "result": bool,
    "data": {
        "name": str,
        "surname": str,
        "email": str,
        "team": int
    }
}
```

### Update User information
Endpoint: `http://127.0.0.1:8000/user/update_email/`  
Method: `PUT`  
Request Body:
```json
{
    "email": str,
    "new_email": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```

### Delete User information
Endpoint: `http://127.0.0.1:8000/user/delete/`  
Method: `DELETE`  
Request Body:
```json
{
    "email": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```

### Create a Team
Endpoint: `http://127.0.0.1:8000/team/create/`  
Method: `POST`  
Request Body:
```json
{
    "name": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```


### Get Team information
Endpoint: `http://127.0.0.1:8000/team/info/`  
Method: `GET`  
Request Body:
```json
{
    "team_name": str
}
```

Response:
```json
{
    "result": bool,
    "info": str,
    "data": {
        "name": str,
        "members": [
            {
                "id": int,
                "email": str,
                "name": str,
                "surname": str,
                "team_id": int
            }
        ]
    }
}
```


### Update Team information
Endpoint: `http://127.0.0.1:8000/team/update/`  
Method: `PUT`  
Request Body:
```json
{
    "team_name": str,
    "new_team_name": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```

### Delete User information
Endpoint: `http://127.0.0.1:8000/team/delete/`  
Method: `DELETE`  
Request Body:
```json
{
    "team_name": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```

### Adding a user to a group
Endpoint: `http://127.0.0.1:8000/user/add_to_team/` 
Method: `POST`  
Request Body:
```json
{
    "email": str,
    "name_team": str
}
```

Response:
```json
{
    "result": bool,
    "info": str
}
```




### Getting Started
To run the project, follow these steps:

1. Install project dependencies using Poetry:
   ```
   poetry install
   ```

2. Navigate to the app directory:
   ```
   cd .\app\
   ```

3. Run the main Python file using Poetry:
   ```
   poetry run python main.py
   ```

The API server will start locally at `http://127.0.0.1:8000/`.

Happy coding! 🚀
