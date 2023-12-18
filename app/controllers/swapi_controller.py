from flask import Blueprint, current_app, request
from requests.exceptions import RequestException

from app import db
from app.models.cache_model import Cache
from app.utils.api_utils import success_response, error_response
from app.utils.swapi_utils import fetch_swapi_data
from constants import KeyConstants

swapi_bp = Blueprint('swapi', __name__, url_prefix='/swapi')

@swapi_bp.route('/<resource>', methods=['GET'])
def get_swapi_data(resource):
    try:
        if not is_valid_resource(resource):
            return error_response(f"Invalid resource provided: {resource}.")
        
        page = int(request.args.get(KeyConstants.SWAPI_PAGE, current_app.config.get('SWAPI_DEFAULT_PAGE')))
        items_per_page = int(request.args.get(KeyConstants.SWAPI_ITEMS_PER_PAGE, current_app.config.get('SWAPI_DEFAULT_ITEMS_PER_PAGE')))
        sort_by = request.args.get(KeyConstants.SWAPI_SORT, current_app.config.get('SWAPI_DEFAULT_SORT'))
        order_by = request.args.get(KeyConstants.SWAPI_ORDER, current_app.config.get('SWAPI_DEFAULT_ORDER'))
        search_term = request.args.get(KeyConstants.SWAPI_SEARCH, current_app.config.get('SWAPI_DEFAULT_SEARCH'))

        # Fetch data from the database
        cache_entry = Cache.query.filter_by(resource_name=resource).first()

        if not cache_entry:
            # If data for the resource doesn't exist in the database, fetch all SWAPI data and store it in the database
            db_data = fetch_swapi_data(resource)
            store_data_in_db(resource, db_data)
        else:
            # If data exists, fetch it from the database
            db_data = eval(cache_entry.data)

        # Perform filtering based on search term
        filtered_data = filter_data(db_data, search_term)

        # Perform sorting based on the specified attribute
        sorted_data = sort_data(filtered_data, sort_by, order_by)

        # Perform pagination
        paginated_data, pagination_info = paginate_data(sorted_data, page, items_per_page)

        return success_response(paginated_data, pagination=pagination_info, message=f"Data retrieved for {resource}")
    
    except RequestException as re:
        current_app.logger.error(f"Request error while fetching SWAPI data: {str(re)}")
        return error_response("Error connecting to SWAPI.")

    except Exception as e:
        current_app.logger.error(f"Error while processing request: {str(e)}")
        return error_response("Internal server error")

@swapi_bp.route('/<resource>/<id>', methods=['GET'])
def get_swapi_data_with_id(resource, id):
    try:
        if not is_valid_resource(resource):
            return error_response(f"Invalid resource provided: {resource}.")
        
        # If data for the resource doesn't exist in the database, fetch all SWAPI data and store it in the database
        db_data = fetch_swapi_data(resource, id)

        return success_response(db_data, message=f"Data retrieved for {resource} with id {id}")
    
    except RequestException as re:
        current_app.logger.error(f"Request error while fetching SWAPI data for resource {resource} with id {id}: {str(re)}")
        return error_response(f"Error connecting to SWAPI: {str(re)}")

    except Exception as e:
        current_app.logger.error(f"Error while processing request for resource {resource} with id {id}: {str(e)}")
        return error_response(f"Internal server error for resource {resource} with id {id}.")

def is_valid_resource(resource):
    return resource in current_app.config.get('SWAPI_RESOURCES')

def store_data_in_db(resource, data):
    current_app.logger.info(f"Storing data for {resource} in the database...")
    # Check if the resource_name already exists in the database
    cache_entry = Cache.query.filter_by(resource_name=resource).first()

    if cache_entry:
        # If the resource_name exists, update the existing row
        cache_entry.data = str(data)
        db.session.commit()
    else:
        # If the resource_name does not exist, create a new row
        new_cache_entry = Cache(resource_name=resource, data=str(data))
        db.session.add(new_cache_entry)
        db.session.commit()

def filter_data(data, search_term):
    # Implement your specific search logic here
    if not search_term:
        return data

    current_app.logger.info(f"Filtering data based on search term: {search_term}")
    filtered_data = [item for item in data if search_term.lower() in str(item).lower()]
    return filtered_data

def sort_data(data, sort_by, order_by):
    # Implement your specific sorting logic here
    if not sort_by:
        return data

    current_app.logger.info(f"Sorting data based on {sort_by} in {order_by} order")
    try:
        # Use SQLAlchemy's order_by for dynamic sorting
        return sorted(data, key=lambda x: x.get(sort_by, ""), reverse=order_by.lower() != current_app.config.get('SWAPI_DEFAULT_ORDER'))

    except KeyError:
        current_app.logger.warning(f"Invalid sort attribute: {sort_by}. Sorting skipped.")
        return data

def paginate_data(data, page, items_per_page):
    current_app.logger.info("Paginating data...")
    total_items = len(data)
    total_pages = (total_items + items_per_page - 1) // items_per_page

    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    paginated_data = data[start_idx:end_idx]

    pagination_info = dict(
        current_page=page,
        total_pages=total_pages,
        total_items=total_items,
        items_per_page=items_per_page,
        prev_page=page - 1 if page > 1 else None,
        next_page=page + 1 if page < total_pages else None
    )

    return paginated_data, pagination_info

def update_cache_data():
    current_app.logger.info("Updating cache data...")
    # Create the database tables if they do not exist
    db.create_all()
    for resource in current_app.config.get('SWAPI_RESOURCES'):
        data = fetch_swapi_data(resource)
        store_data_in_db(resource, data)
        current_app.logger.info(f"{resource} cache data updated successfully.")
    current_app.logger.info("All cache data updated successfully.")
