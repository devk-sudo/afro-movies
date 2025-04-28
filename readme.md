# AfroMovies API

A powerful and developer-friendly API for accessing African movie data and global cinema.

## Overview

The AfroMovies API provides comprehensive access to a rich database of African movies and global cinema.  
It allows developers to retrieve movie information, manage user accounts, and handle user-specific data like favorites and cart items.  
The API is designed to be flexible and easy to integrate into various applications.

## Features

- **Movie Data Access**: Retrieve detailed information about movies, including titles, genres, release dates, ratings, and more.
- **User Management**: Register and authenticate users, manage favorites, and handle cart items.
- **Authentication**: Secure endpoints with JWT (JSON Web Tokens).
- **Rate Limiting**: Supports different tiers (Free, Developer, Professional, Enterprise) with varying request limits.
- **SDK Libraries**: Official client libraries for JavaScript, Python, PHP, and Java.
- **Comprehensive Documentation**: Detailed API documentation with examples in multiple programming languages.

## Getting Started

### Base URL

```
https://afro-movies-api.onrender.com
```

### Authentication

Protected endpoints require a JWT token in the `Authorization` header:

```
Authorization: Bearer <your-jwt-token>
```

### Example Request

Fetch all movies using JavaScript:

```javascript
fetch('https://afro-movies-api.onrender.com/api/movies/all')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```

## Installation

To use the API, you can make HTTP requests directly or use one of our official SDK libraries:

- **JavaScript**: [Documentation](#)
- **Python**: [Documentation](#)
- **PHP**: [Documentation](#)
- **Java**: [Documentation](#)

## Usage

### Key Endpoints

#### Movies

- `GET /api/movies/all`: Retrieve all movies.
- `GET /api/movies/{id}`: Get a specific movie by ID.
- `GET /api/movies/latest`: Get the latest movies.
- `GET /api/movies/popular`: Get popular movies.
- `GET /api/movies/category/{category}`: Get movies by category.

#### Users

- `POST /api/users/register`: Register a new user.
- `POST /api/users/login`: Log in and receive a JWT token.
- `GET /api/users/favorites`: Get user favorites (authenticated).
- `POST /api/users/favorites`: Add a movie to favorites (authenticated).
- `GET /api/users/cart`: Get user cart items (authenticated).
- `POST /api/users/cart`: Add a movie to cart (authenticated).

## Rate Limits

- **Free**: 100 requests/hour
- **Developer**: 1,000 requests/hour
- **Professional**: 10,000 requests/hour
- **Enterprise**: Custom

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:  
   ```bash
   git commit -m 'Add your feature'
   ```
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For support or inquiries, please contact us at [support@afromoviesapi.com](mailto:support@afromoviesapi.com).
