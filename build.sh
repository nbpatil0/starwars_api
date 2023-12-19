#!/bin/bash

# Set up Python virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Gunicorn
exec gunicorn -b :$PORT --timeout 120 app:app
