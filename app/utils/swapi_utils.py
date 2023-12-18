from flask import current_app
import requests

from constants import KeyConstants


def get_swapi_data(url):
    current_app.logger.info(f"Fetching data from {url}")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_swapi_data(resource, id=None):
    url = current_app.config.get('SWAPI_BASE_URL') + resource
    if id:
        url += f"/{id}"
        return get_swapi_data(url)
    
    result = []

    while url:
        data = get_swapi_data(url)
        result.extend(data.get(KeyConstants.SWAPI_RESULTS, []))
        url = data.get(KeyConstants.SWAPI_NEXT)

    return result
