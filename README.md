# Star Wars API Caching Engine

This project provides a caching engine for the Star Wars API ([SWAPI](https://swapi.dev/)) to enhance its features for high school students working on school projects.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Dockerfile](#dockerfile)
- [Usage](#usage)
- [Unit Tests](#unit-tests)
- [Cron Job](#cron-job)
- [Loggers](#loggers)
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

## Dockerfile

A Dockerfile is included to containerize the application for easy deployment and isolation. Follow the instructions below to run the Dockerized application locally:

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.

### Build and Run

1. Open a terminal and navigate to the project directory.

2. Build the Docker image:

   ```bash
   docker build -t starwars-api-server .
   ```

3. Run the Docker container:

   ```bash
   docker run -p 5000:5000 starwars-api-server
   ```

   The application will be accessible at http://127.0.0.1:5000/.

## Usage

### API Endpoints

- `/swapi/<resource>`: Retrieve data for a specific Star Wars resource with query parameters defined below.
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

## Loggers

Logging has been implemented throughout the application to capture important events and errors. Loggers help in monitoring and troubleshooting the application.

## Deployment

To deploy the application on a remote server, follow the deployment procedures for your chosen hosting platform.

### Deployment on Render

The Star Wars API Caching Server has been deployed on the Render platform. Please note the following considerations:

- **Service Limitations:**

  - Render services have a limitation where if the server doesn't receive any inbound hits for 15 minutes, the server shuts down to conserve resources.
  - The server will start automatically upon receiving a new incoming request.

- **Initialization Time:**

  - As part of the deployment process, the server first updates the cache data from the Star Wars API.
  - It may take a few minutes for the server to respond to the first API request, especially during the initial cache update.

- **Example:**

  - Retrieve data for a specific Star Wars resource with Search and Sort:

  ```bash
  https://starwars-api-7nk0.onrender.com/swapi/starships?items_per_page=20&search=transport&sort=cargo_capacity
  ```

  - Retrieve details for a specific item within a resource:

  ```bash
  https://starwars-api-7nk0.onrender.com/swapi/starships/2
  ```
