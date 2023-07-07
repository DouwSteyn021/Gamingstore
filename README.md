# Gaming Store

This is a Django-based gaming store web application.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone repository
   git clone <repository_url>

Change project directory:
   cd gamingstore

2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate

3. Install the project dependencies:
   pip install -r requirements.txt

4. Apply database migrations:
   python manage.py migrate

To run the development server, use the following command:
   python manage.py runserver
   The web application will be accessible at http://localhost:8000.

## Documentation

The documentation for this project is generated using Sphinx. You can find the user-friendly documentation in the docs/build directory.

To generate the documentation, run the following command:
   sphinx-build -b html docs docs/build

## Docker

To run the project using Docker, follow these steps:

1. Build the Docker image:
   docker build -t gamingstore .

2. Run a Docker container:
   docker run -p 8000:8000 gamingstore

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the name of the author: "Douw Steyn"

