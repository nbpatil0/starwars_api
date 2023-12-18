import json
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = os.getenv('LOG_FILE')
    CRON_INTERVAL = int(os.getenv('CRON_INTERVAL'))
    SWAPI_BASE_URL = os.getenv('SWAPI_BASE_URL', 'https://swapi.dev/api/')
    SWAPI_RESOURCES = json.loads(os.getenv("SWAPI_RESOURCES", '["films", "people", "planets", "species", "starships", "vehicles"]'))
    SWAPI_DEFAULT_PAGE = int(os.getenv('SWAPI_DEFAULT_PAGE', 1))
    SWAPI_DEFAULT_ITEMS_PER_PAGE = int(os.getenv('SWAPI_DEFAULT_ITEMS_PER_PAGE', 10))
    SWAPI_DEFAULT_SORT = os.getenv('SWAPI_DEFAULT_SORT', 'name')
    SWAPI_DEFAULT_ORDER = os.getenv('SWAPI_DEFAULT_ORDER', 'asc')
    SWAPI_DEFAULT_SEARCH = os.getenv('SWAPI_DEFAULT_SEARCH', '')
