

# DRF Personal Blog

https://www.youtube.com/watch?v=c708Nf0cHrs

A blogging platform built with Django REST Framework (DRF) for personal use and hobbyist blogging. This project allows users to create, read, update, and delete blog posts.

## Table of Contents

- [DRF Personal Blog](#drf-personal-blog)
  - [Table of Contents](#table-of-contents)
  - [Use Case](#use-case)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Install Dependencies](#install-dependencies)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Technologies Used](#technologies-used)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

## Use Case

This platform is created for my blogging hobby. It serves as a personal space to share thoughts, ideas, and content with others.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **CRUD Operations**: Create, read, update, and delete blog posts.
- **API-Driven**: Built with Django REST Framework to provide a RESTful API.
- **Responsive Design**: Designed to be accessible and user-friendly across devices.

## Installation

To set up the project locally, follow these steps:

### Prerequisites

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Once the setup is complete, you can access the blog platform locally at `http://localhost:8000`. Use the superuser credentials to log in to the Django admin panel and manage blog posts.

## API Endpoints

Here are some key API endpoints provided by the Django REST Framework:

- `GET /api/posts/`: List all blog posts
- `POST /api/posts/`: Create a new blog post
- `GET /api/posts/{id}/`: Retrieve a specific blog post
- `PUT /api/posts/{id}/`: Update a specific blog post
- `DELETE /api/posts/{id}/`: Delete a specific blog post

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is not licensed for any use cases.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
