

 FastAPI MVC Web Application

This is a FastAPIbased web application following the MVC (ModelViewController) design pattern. It includes user authentication, post management, and inmemory caching. The application uses SQLAlchemy for database interactions, Pydantic for data validation, and Redis for caching.



 Features

 User Authentication:
   Signup with email and password.
   Login with email and password to receive a JWT token.
 Post Management:
   Add a new post (with tokenbased authentication).
   Get all posts for a user (with tokenbased authentication and caching).
   Delete a post (with tokenbased authentication).
 Database:
   MySQL database with SQLAlchemy ORM.
 Caching:
   Inmemory caching using Redis for the `GetPosts` endpoint (cached for 5 minutes).
 Validation:
   Extensive field validation using Pydantic models.
 Testing:
   Unit tests for models, services, and controllers.



 Prerequisites

Before running the application, ensure you have the following installed:

 Python 3.8+
 MySQL (or any compatible database)
 Redis (for caching)
 pip (Python package manager)


 Setup
pip install r requirements.txt

Copy the `.env` template:
 cp sample.env .env


 Set Up the Database

Create a MySQL database:
   ```sql
   CREATE DATABASE fastapi_app;
   ```
 Run the application to create the tables:
   ```bash
   uvicorn app.main:app reload
   ```



 Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app reload
   ```
2. The application will be available at:
   ```
   http://127.0.0.1:8000
   ```



 API Endpoints

 1. Signup
 URL: `/signup`


 2. Login
 URL: `/login`

 3. Add Post
 URL: `/addpost`
 Headers:
  ```
  Authorization: Bearer <yourjwttoken>
  ```

 4. Get Posts
 URL: `/getposts`

 Headers:
  ```
  Authorization: Bearer <yourjwttoken>
  ```


 5. Delete Post
 URL: `/deletepost`

 Headers:
  ```
  Authorization: Bearer <yourjwttoken>
  ```



 Running Tests

To run the unit tests, use the following command:

```bash
pytest
```


 Project Structure

```
fastapi_mvc_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── user.py
│   │   └── post.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── post.py
│   ├── controllers/
│   │   └── __init__.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── post_service.py
│   ├── repositories/
│   │   └── __init__.py
│   └── dependencies.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_services.py
│   └── test_controllers.py
├── .env
├── sample.env
├── .gitignore
├── requirements.txt
└── README.md
```



 Technologies Used

 Python: Programming language.
 FastAPI: Web framework for building APIs.
 SQLAlchemy: ORM for database interactions.
 Pydantic: Data validation and settings management.
 Redis: Inmemory caching.
 JWT: Tokenbased authentication.
 Pytest: Testing framework.




 Contact

For any questions or feedback, please contact:
wondimagegn Zewudu
 Email: wondeis2018@gmail.com,wondimagagnzewudu@gmail.com
 GitHub: [wondimagagnzewudu](https://github.com/wondimagagnzewudu)



