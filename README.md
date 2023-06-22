# Short URL Generator

![Short URL Generator](https://free-url-shortener.rb.gy/url-shortener.png)

Short URL Generator is a backend project developed using [FastAPI](https://fastapi.tiangolo.com/) and [MongoDB](https://www.mongodb.com/). It provides a service for generating short and unique aliases (short links) for long URLs. Users can generate short links, set custom aliases, and manage their URLs through a simple and efficient API.

## Features

- Generate a short and unique alias for a given long URL.
- Optionally set a custom alias for the URL.
- URLs can be set to expire after a specified timeframe.
- User authentication and authorization using OAuth2 with Google Sign-In.
- Users can create short URLs and manage their own URLs.
- Secure storage of user details and URLs in the MongoDB database.
- Fast and efficient API endpoints for creating and deleting URLs.
- Data validation using Pydantic models.
- Simple and easy-to-understand code structure.

## Installation

Make sure you have [Python](https://www.python.org/) and [MongoDB](https://www.mongodb.com/) installed on your system.

1. Clone the repository:

```bash
git clone https://github.com/abhishek7kalra/short-url-generator.git
```

2. Navigate to the project directory:

```bash
cd short-url-generator
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the environment variables:

Create a `.env` file in the root directory and add the following variables:

```plaintext
MONGO_HOST=<mongodb_host>
MONGO_PORT=<mongodb_port>
MONGO_DB_NAME=<mongodb_database_name>
MONGO_USERNAME=<mongodb_username>
MONGO_PASSWORD=<mongodb_password>
JWT_SECRET=<jwt_secret_key>
GOOGLE_CLIENT_ID=<google_client_id>
```

Make sure to replace `<mongodb_host>`, `<mongodb_port>`, `<mongodb_database_name>`, `<mongodb_username>`, `<mongodb_password>`, `<jwt_secret_key>`, and `<google_client_id>` with your actual values.

5. Start the application:

```bash
uvicorn main:app --reload
```

You can now access the API endpoints at `http://localhost:8000`.

## API Endpoints

- `POST /createUrl` - Create a short URL
- `DELETE /deleteUrl/{url_id}` - Delete a short URL
- `POST /signup` - Create a new user
- `POST /login` - Authenticate a user
- `GET /profile` - Retrieve user profile

For detailed API documentation, visit `http://localhost:8000/docs` or `http://localhost:8000/redoc`.

## Contributing

Contributions are welcome! If you find any bugs, create an issue or submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast, web framework for building APIs with Python 3.7+.
- [MongoDB](https://www.mongodb.com/) - NoSQL database for storing user data and URLs.
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and parsing using Python type annotations.
- [Python JWT](https://github.com/jpadilla/pyjwt) - Library for encoding and decoding JSON Web Tokens (JWTs).
- [Passlib](https://passlib.readthedocs.io/en/stable/) - Password hashing and verification library.

"Short URL Generator" is an open-source project developed by [Abhishek Kalra](https://github.com/abhishek7kalra).
