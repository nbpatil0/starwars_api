# Star Wars API Caching Engine

This project provides a caching engine for the Star Wars API ([SWAPI](https://swapi.dev/)) to enhance its features for high school students working on school projects.

## Features

- **REST API:** Designed to serve the needs of high school students with additional features like search, sort, etc.
- **Caching:** Utilizes SQLite for caching SWAPI data, providing faster responses and reducing the load on the SWAPI server.
- **Modular Design:** Follows a modular structure with controllers, models, and utilities.
- **Logging:** Implements logging for better visibility into the application's behavior.
- **Exception Handling:** Handles exceptions gracefully to ensure the stability of the application.
- **Unit Tests:** Includes unit tests for the SWAPI controller.
- **Cron Job:** Sets up a cron job using APScheduler to periodically update the cached data.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file based on the provided example.

## Usage

1. Run the Flask application: `flask run`.
2. Access the API endpoints at `http://127.0.0.1:5000/swapi/<endpoint>`.

## Testing

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
