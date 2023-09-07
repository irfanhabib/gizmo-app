# gizmo-app

This is a simple REST API built using Flask, which connects to a Postgres database. The project also uses pydantic for request validation and serialization.

## Getting Started

### Prerequisites

- Python 3.10 or above
- poetry
- PostgreSQL 13
- Docker and Docker Compose (Optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/irfanhabib/gizmo-app.git
```

2. Change to the project directory:
```bash
cd gizmo-app
```

3. Install the required packages:
```bash
poetry install
```

4. Set up your PostgreSQL database and adjust the database URI in the `config.py`.

5. Setup environment variables

``` bash
source .env
```


5. Initialize the database:
```bash
flask db upgrade
```

## Running the App

1. Run the app using Flask's built-in server:
```bash
make run
```

### Using Docker (Optional)

1. Start the services:
```bash
make up
```

2. Stop the services:
```bash
make down
```

## Running Tests

To run the tests, execute the following command:

```bash
pytest test_app.py
```

## Usage

This API has the following endpoints:

- Create an example record: `POST /api/v1/example`
- Read an example record: `GET /api/v1/example/<id>`
- Update an example record: `PUT /api/v1/example/<id>`
- Delete an example record: `DELETE /api/v1/example/<id>`

### Create

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "example"}' http://localhost:8000/api/v1/example
```

### Read

```bash
curl http://localhost:8000/api/v1/example/1
```

### Update

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "updated_example"}' http://localhost:8000/api/v1/example/1
```

### Delete

```bash
curl -X DELETE http://localhost:8000/api/v1/example/1
```

## Makefile Commands

- Lint the project: `make lint`
- Run tests: `make test`
- Start services using docker-compose: `make up`
- Stop services using docker-compose: `make down`

---
