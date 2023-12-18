FROM python:3.11

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN python -m venv venv
RUN . venv/bin/activate && pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the app will run
EXPOSE $PORT

# Run the application
CMD ["./build.sh"]
