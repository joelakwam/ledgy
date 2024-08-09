# LEDGY RESTful API

This project is a Django-based RESTful API for keeping track of your **INCOME** and **EXPENSE** statements. The API allows you to perform CRUD (Create, Read, Update, Delete) operations on statements and includes user authentication using JWT (JSON Web Tokens).

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

----

## Features

- **CRUD operations**: Manage books with create, read, update, and delete functionalities.
- **JWT Authentication**: Secure the API using JSON Web Tokens.
- **Django REST Framework**: Utilizes Django REST Framework for building the API.

---

## Technologies Used

- **Python**: The core programming language.
- **Django**: The web framework used to build the application.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **SQLite**: The default database used for development.
- **djangorestframework-simplejwt**: Provides JWT authentication.

---

## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/joelakwam/ledgy.git
   cd ledgy
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv ledgy
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the API:**
   - Visit `http://localhost:8000/api/` in your web browser.

----

## API Endpoints

### Statements

- **List all statements**: `GET /api/statements/`
- **Create a new statement**: `POST /api/statements/`
- **Retrieve a single statement**: `GET /api/statements/<int:pk>/`
- **Update a statement**: `PUT /api/statements/<int:pk>/`
- **Delete a statement**: `DELETE /api/statements/<int:pk>/`

### Authentication

- **Obtain JWT token**: `POST /api/token/`
- **Refresh JWT token**: `POST /api/token/refresh/`
- **Access protected resource**: `GET /api/protected/`

----

## Authentication

This project uses JWT for securing the API. You need to obtain a token via the `/api/token/` endpoint and include it in the `Authorization` header as a Bearer token for protected endpoints.

Example of obtaining a JWT token:
```bash
curl -X POST http://localhost:8000/api/token/ -d "username=yourusername" -d "password=yourpassword"
```

Use the token for accessing protected resources:
```bash
curl -H "Authorization: Bearer <ACCESS_TOKEN>" http://localhost:8000/api/protected/
```

----

## Testing the API

You can test the API using tools like `curl`, Postman, or any other API testing tool.

### Example Commands

- **Create a new statement:**
  ```bash
  curl -X POST http://localhost:8000/api/statements/ -H "Authorization: Bearer <ACCESS_TOKEN>" -d "title=Sample Title" -d "description=Test Description"
  ```

- **Get all statements:**
  ```bash
  curl -X GET http://localhost:8000/api/statements/ -H "Authorization: Bearer <ACCESS_TOKEN>"
  ```

- **Update a statement:**
  ```bash
  curl -X PUT http://localhost:8000/api/statements/1/ -H "Authorization: Bearer <ACCESS_TOKEN>" -d "title=Updated Title"
  ```

- **Delete a book:**
  ```bash
  curl -X DELETE http://localhost:8000/api/statements/1/ -H "Authorization: Bearer <ACCESS_TOKEN>"
  ```

----
## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

----

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

