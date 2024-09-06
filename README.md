# URL Shortener Service

## Table of Contents
- [Description](#description)
- [Feautres](#features)
- [Instalation](#instalation)
- [API Endpoints](#api-endpoints)
- [Future Improvements](#future-improvements)
- [License](#license)

## Description
A simple URL shortener service built using Flask and MySQL. This service allows users to shorten long URLs and redirect to the original URLs.

## Features
- **Shorten URLs:** Convert long URLs into short, manageable links.
- **Redirect to Original URL:** Redirect users from short URLs to their original destinations.
- **Database Storage:** MySQL is used to store URL mappings.

## Instalation

### Prerequisites
- Python 3.10.6
- MySQL Server

### Steps
1. Clone the Repository

    ```bash
    Copy code
    git clone https://github.com/yourusername/url-shortener-service.git
    cd url-shortener-service
    ```

2. Create and Activate a Virtual Environment

    ```bash
    Copy code
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Set Up the Database

    - Start your MySQL server.
    - Create a new database called mydatabase and set up the required schema.

    **SQL Script to Initialize the Database:**

    ```sql
    Copy code
    CREATE DATABASE mydatabase;
    USE mydatabase;

    CREATE TABLE IF NOT EXISTS urls (
        id INT AUTO_INCREMENT PRIMARY KEY,
        original_url TEXT NOT NULL,
        shortened_path VARCHAR(255) UNIQUE NOT NULL
    );
    ```

5. **Configure the Flask Application**

    Update the database connection URL in your Flask configuration file to match your MySQL server settings.

    **Example configuration in `app/config.py`:**

    ```python
    Copy code
    import os

    class Config:
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:password@localhost:3306/mydatabase')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

6. Run the Flask Application

    Ensure the MySQL server is running and start your Flask application:

    ```bash
    flask run
    ```
    This will start the Flask app on `http://localhost:5000`.

## API Endpoints
- `POST /api/` - Shortenes the url and maps it into the database
- `GET /api/<shortened_url>` - Redirectes the shortened url to it's original url

For a complete list of endpoints and their usage, refer to the OpenAPI documentation available at `http://localhost:5000` after running the spring-boot application.

## Technologies Used
- **Flask**
- **Flask-SQLAlchemy**
- **MySQL**
- **SQLAlchemy**
- **PyMySQL**

## Future Improvements
1. **Custom Header Authentication for Redirects**
    - Introduce authentication mechanisms (e.g., API keys, OAuth) to make querying redirects more secure, especially for use cases that involve sensitive or private links.
2. **POST Request for Redirect**
    - Implement a POST request that accepts the shortened_path in the body of the request, rather than as part of the URL. This could make the API more versatile and enhance security.

## License
This project is licensed under the GNU General Public License v3.0 License. See the [LICENSE](./LICENSE) file for details