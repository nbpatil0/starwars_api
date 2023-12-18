from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

from app.utils.logger_utils import setup_logger
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.controllers.cron_controller import update_cache
from app.controllers.swapi_controller import swapi_bp

app.register_blueprint(swapi_bp)


setup_logger(app)

update_cache()

# Set up the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(update_cache, 'interval', seconds=app.config.get('CRON_INTERVAL'))
scheduler.start()

# Ensure that the scheduler shuts down cleanly on exit
atexit.register(lambda: scheduler.shutdown())
