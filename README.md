# simple-django-api

This Django REST Framework project makes part of my portfolio. It provides a simple API for managing service endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

You need to have Python and Django installed on your machine. You can download Python
from [here](https://www.python.org/downloads/) and you can install Django using pip:

```bash
pip install django
```

You also need to install Django REST Framework:

```bash
pip install djangorestframework
```

### Installing

Clone the repository:

```bash
git clone https://github.com/santannaflaercio/simple-django-api.git
```

Navigate to the project directory:

```bash
cd simple_django_api
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the migrations:

```bash
python manage.py migrate
```

Finally, start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Running the tests

To run the tests, use the following command:

```bash
python manage.py test
```

## Built With

* [Python](https://www.python.org/) - The programming language used
* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - The toolkit used to build the API

## Authors

* **santannaflaercio** - *Initial work* - [santannaflaercio](https://github.com/santannaflaercio)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
