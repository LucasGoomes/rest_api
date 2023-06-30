# Python FastAPI REST API

This is an example of a Python REST API using the FastAPI framework. The API allows performing basic operations on blogs and users.

## Introduction

This API has been developed using FastAPI, a modern and efficient framework for building APIs in Python. It provides endpoints for creating, reading, updating, and deleting blogs, as well as creating and retrieving user information.

The API uses SQLAlchemy as the database ORM for storing blog and user data. The database can be configured in the `database.py` file. Please ensure that you configure the database connection information correctly before running the API.

User password authentication is performed using the Bcrypt hashing algorithm provided by the `passlib` library. This ensures the security of stored passwords in the database.

The API follows a modular structure, with data models defined in `models.py`, validation schemas in `schemas.py`, and route handling and operations in the respective endpoints defined in `main.py`.

## Endpoints

The API includes the following endpoints:

### Create a New Blog

- **Method:** `POST`
- **URL:** `/blog`
- **Response Status:** `201 Created`
- **Tags:** `blogs`

Creates a new blog based on the data provided in the request body.

### Get All Blogs

- **Method:** `GET`
- **URL:** `/blog`
- **Response Status:** `200 OK`
- **Tags:** `blogs`

Retrieves all blogs stored in the database.

### Get a Specific Blog

- **Method:** `GET`
- **URL:** `/blog/{id}`
- **Response Status:** `200 OK`
- **Tags:** `blogs`

Retrieves a specific blog based on the provided ID.

### Update a Blog

- **Method:** `PUT`
- **URL:** `/blog/{id}`
- **Response Status:** `202 Accepted`
- **Tags:** `blogs`

Updates an existing blog based on the provided ID and the data provided in the request body.

### Delete a Blog

- **Method:** `DELETE`
- **URL:** `/blog/{id}`
- **Response Status:** `204 No Content`
- **Tags:** `blogs`

Deletes a blog based on the provided ID.

### Create a New User

- **Method:** `POST`
- **URL:** `/user`
- **Response Status:** `201 Created`
- **Tags:** `users`

Creates a new user based on the data provided in the request body.

### Get a Specific User

- **Method:** `GET`
- **URL:** `/user/{id}`
- **Response Status:** `200 OK`
- **Tags:** `users`

Retrieves a specific user based on the provided ID.

## Running the API

To run the API, ensure that you have the required dependencies installed and execute the following command:

```
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## Notes

- Make sure that the `main.py` file is correctly named and located at the root of the project.
- By default, the API uses a SQLite database. If you wish to use a different database, make the necessary changes to the database configuration in `database.py`.

Feel free to modify the API according to your needs!