# mwdefine

A simple Python CLI tool to fetch word definitions from the Merriam-Webster Dictionary API.

---

## Features

- Fetches English word definitions via the [Merriam-Webster Dictionary API](https://dictionaryapi.com/).
- Easy-to-use command-line interface.
- Minimal dependencies.

---

## Requirements

- Python 3.7+
- [Merriam-Webster Dictionary API Key](https://dictionaryapi.com/account/my-keys)
- Internet connectivity

---

## Installation

Clone this repository:

```sh
git clone https://github.com/Sagar2366/mwdefine.git
cd mwdefine
```

---

## Using a Python Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate
```

Install the package and its dependencies:

```sh
pip install .
```

---

## Getting a Merriam-Webster API Key

1. Go to [https://dictionaryapi.com/account/my-keys](https://dictionaryapi.com/account/my-keys).
2. Sign up or log in.
3. Register a new application if needed.
4. Copy your API key from the dashboard.

Set your API key as an environment variable (required):

```sh
export MW_API_KEY=your_actual_api_key
```

---

## Usage

### Command Line

```sh
mwdefine <word>
```

**Example:**

```sh
mwdefine example
```

You can also pass the API key directly:

```sh
mwdefine exercise --api-key=your_actual_api_key
```

Show the raw API response:

```sh
mwdefine example --raw
```

---

## Makefile Commands

- Build and test everything:

  ```sh
  make all
  ```

- Build the package and install dependencies:

  ```sh
  make build
  ```

- Run all tests:

  ```sh
  make test
  ```

- Build a PyPI artifact:

  ```sh
  make artifact
  ```

- Clean build artifacts:

  ```sh
  make clean
  ```

---

## Project Structure

```plaintext
mwdefine/
├── __init__.py          # Marks the directory as a Python package
├── api.py               # Merriam-Webster API logic and entry class
├── cli.py               # CLI entry point (mwdefine command)
├── formatter.py         # Output formatting
tests/
└── test_api.py          # Tests for API logic
setup.py                 # Package metadata and entry points
Makefile                 # Build and test automation
README.md                # This file
.github/
└── workflows/
    └── ci.yaml          # GitHub Actions for CI/CD
```
