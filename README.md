# Star Wars API Caching Engine

This project provides a caching engine for the Star Wars API ([SWAPI](https://swapi.dev/)) to enhance its features for high school students working on school projects.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Unit Tests](#unit-tests)
- [Cron Job](#cron-job)
- [Deployment](#deployment)

## Features

- **REST API:** Designed to serve the needs of high school students with additional features like search, sort, etc.
- **Caching:** Utilizes SQLite for caching SWAPI data, providing faster responses and reducing the load on the SWAPI server.
- **Modular Design:** Follows a modular structure with controllers, models, and utilities.
- **Logging:** Implements logging for better visibility into the application's behavior.
- **Exception Handling:** Handles exceptions gracefully to ensure the stability of the application.
- **Unit Tests:** Includes unit tests for the SWAPI controller.
- **Cron Job:** Sets up a cron job using APScheduler to periodically update the cached data.

## Prerequisites

- Python (>v3.9)
- Pip (Python package installer)
- SQLite (for local development)

## Installation

1. Clone the repository.

   ```bash
   git clone https://github.com/nbpatil0/starwars_api.git
   cd starwars_api
   ```

2. Create a virtual environment and activate it.

   ```bash
   python -m venv venv
   ```

   - on Windows

   ```bash
   venv\Scripts\activate
   ```

   - on Mac/Linux

   ```bash
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file based on the provided example:

   ```bash
   FLASK_APP=app.main:app
   FLASK_ENV=development
   DATABASE_URI=sqlite:///cache.db
   LOG_FILE=app.log
   CRON_INTERVAL=3600
   ```

5. Source the `.env` file:

   ```bash
   source .env
   ```

6. Run the Flask application:
   ```bash
   flask run
   ```

## Usage

### API Endpoints

- `/swapi/<resource>`: Retrieve data for a specific Star Wars resource.
- `/swapi/<resource>/<id>`: Retrieve details for a specific item within a resource.

### Query Parameters

- `page`: Page number for pagination (default: 1)
- `items_per_page`: Number of items per page (default: 10)
- `sort`: Attribute to sort by
- `order`: Sorting order ('asc' or 'desc')
- `search`: Search term

## Unit Tests

Run the unit tests using the following command:

```bash
python -m unittest discover -s tests
```

## Cron Job

The cron job is automatically set up to run every hour (adjustable in the .env file). To manually update the cache, run the following:

```bash
python cron.py
```

## Deployment

To deploy the application on a remote server, follow the deployment procedures for your chosen hosting platform.
