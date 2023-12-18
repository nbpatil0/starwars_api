from app import app
from app.controllers.swapi_controller import update_cache_data

def update_cache():
    with app.app_context():
        update_cache_data()
        