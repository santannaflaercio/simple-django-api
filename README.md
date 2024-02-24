# Simple Django API

[![python](https://img.shields.io/badge/python-v3.10+-blue.svg?logo=python)](https://github.com/topics/python) 
[![calculator](https://img.shields.io/badge/django-API-orange.svg)](https://github.com/topics/calculator)

This repository contains a simple Django REST Framework project that provides an API for managing service endpoints. The
project was developed as part of my portfolio. It is a simple project, but it is a good example of how to build a REST
API using Django.

## How To Run

To run this project, you will need to have Python 3.10 or later installed. If you don't have it, you can download it from
the [official website](https://www.python.org/downloads/). You will also need to have `pip` installed. If you don't have
it, you can follow the instructions on the [official website](https://pip.pypa.io/en/stable/installation/). With Python
and `pip` installed, you can follow the steps below to run the project:

1. Clone the repository:

```bash
git clone
```

2. Navigate to the project's directory:

```bash
cd simple-django-api
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

5. Install the project's dependencies:

```bash
pip install -r requirements.txt
```

6. Run the migrations:

```bash
python manage.py migrate
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Access the API at `http://localhost:8000/api/`.
9. Access the admin interface at `http://localhost:8000/admin/`.

## API Endpoints

The API provides the following endpoints:

- `GET /api/`: returns a list of all services.
- `POST /api/`: creates a new service.

## How to Contribute

Contributions are always welcome! Here's how you can get involved:

- Report any bugs or issues you encounter.
- Suggest new features or enhancements to improve the project.
- Submit pull requests with code improvements or fixes.

We appreciate your contributions and feedback to make this project better!

## License

This project is released without a license. You are free to use it for any purpose.