# Polling Place Analysis

This project is designed to analyze polling place data from a CSV file and interact with a SQLite database. It includes functionalities for extracting data from CSV, loading data into the database, performing CRUD operations, and querying the database.

## Project Structure

```
project
├── .devcontainer/          # Dev container configuration
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/                # GitHub actions for CI/CD pipeline
│   └── workflows/cicd.yml
├── Data/                   # Data folder containing CSV files
│   └── polling_place_20240514.csv
├── mylib/                  # Python library for data extraction, loading, and querying
│   ├── extractData.py
│   ├── loadData.py
│   └── queryData.py
├── test.py                 # Test file to verify the CRUD operations
├── Makefile                # Makefile for easy task execution
├── README.md               # Project documentation
├── Requirements.txt        # Python dependencies
├── database1.db            # SQLite database (created during runtime)
├── testOutputs.md          # Test output logs
└── queryLog.md             # SQL query logs
```

## Requirements

- Python 3.9+
- SQLite 3

### Installing Dependencies

To install all required dependencies, run:

```bash
make install
```

This will install the necessary Python packages listed in `requirements.txt` and development tools.

## Running the Project

The main script for interacting with the database is `main.py`. To run the project and perform CRUD operations and queries, simply execute:

```bash
python main.py
```

## Running Tests

To run tests that validate CRUD operations and SQL queries, use:

```bash
make test
```

This will use `pytest` to run all test files (`test*.py`) with verbose output.

## Code Formatting

To format the Python code using `black`, run:

```bash
make format
```

## Linting

To check the code quality using `flake8`, run:

```bash
make lint
```

This runs two `flake8` commands:
- The first checks for critical issues such as syntax errors.
- The second checks for complexity and style violations with custom settings for line length and complexity.

## Logging

- **Test Logs**: Outputs from the tests, including pass/fail information, are stored in `testOutputs.md`.
- **Query Logs**: Every SQL query executed during CRUD operations is logged in `queryLog.md`.

## CI/CD Pipeline

The project is set up with GitHub Actions. The workflow file `.github/workflows/cicd.yml` runs the following steps on every push:
1. Set up Python environment
2. Install dependencies
3. Create a fresh SQLite database
4. Run tests

---

## Makefile Commands

You can use the following `make` commands to streamline development:

- **`make install`**: Install dependencies.
- **`make format`**: Format the code using `black`.
- **`make lint`**: Run `flake8` for code linting.
- **`make test`**: Run the test suite using `pytest`.
- **`make all`**: Run all of the above commands in sequence.

