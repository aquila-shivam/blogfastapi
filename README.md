# FastAPI Blog API

A simple RESTful API for managing blog posts using FastAPI.

## Features

- User authentication with JWT
- CRUD operations for blog data
- Pagination and sorting of blog content

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/aquila-shivam/blogfastapi.git
    cd fastapi-blog-api
    ```

2. **Setup virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # for Linux/Mac, or .\venv\Scripts\activate for Windows
    pip install -r requirements.txt
    ```

3. **Configuration:**

   Update `config.py` with your database connection details.

4. **Run the Application:**

    ```bash
    uvicorn main:app --reload
    ```

    Open [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger documentation.

5. **API Endpoints:**
   - `/docs` : Use FastApi 
   - `/blogs`: CRUD for blog posts
   - `/users`: User authentication and profile management

6. **Authentication:**

   JWT is used for user authentication.

7. **Dockerization:**

    ```bash
    docker build -t fastapi-blog-api .
    docker run -p 8000:80 fastapi-blog-api
    ```

    Open [http://localhost:8000/docs](http://localhost:8000/docs) for the API.

8. **Contributing:**

   Feel free to contribute. Fork, make changes, and submit a pull request.

9. **License:**

   MIT License - see [LICENSE](LICENSE) for details.
