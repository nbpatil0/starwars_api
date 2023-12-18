import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

def setup_logger(app: Flask):
    handler = RotatingFileHandler(app.config.get('LOG_FILE'), maxBytes=10240, backupCount=10)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Logging started...')
