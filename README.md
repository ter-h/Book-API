# Book-API


A simple **False REST API** for managing books, using **raw PostgreSQL**. This project utilises **backend-only, layered architecture**

--- 

## Feature
- Add a new book (`POST /books/`)
- List all books (`GET /books/`)
- Retrieve a single book by ID (`GET /books/<id>`)
- Delete a book (`DELETE /books/<id>`)
- Fully layered architecture:
  - **Controller**: Handles HTTP requests/responses
  - **Service**: Business logic
  - **Repository**: Direct database operations
- PostgreSQL database connection using `psycopg2`
- Marshmallow schemas for request validation and response serialization
- Environment-based configuration (`.env`) for secure credentials
- Easy to run and test

## Structure

**run.py**: Entry point for Flask application
**requirements.txt**: Python dependencies
**schema.sql**: SQL file defining database tables
**app/**: Main application package
**init.py**: Flask app factory; registers controllers
**config.py**: Database configuration (reads from .env)
**db.py**: Database connection helper using psycopg2
**schemas.py**: Marshmallow schemas for validation/serialisaition
**controllers/ - book_controller.py**: HTTP endpoints (Flask Blueprints)
**services/ - book_service.py**: Business logic layer
**repository/ - book_db.py**: Data access layer

## How to Run Everything
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

createdb bookdb
psql bookdb < schema.sql

python run.py
```