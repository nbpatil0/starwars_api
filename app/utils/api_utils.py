from flask import jsonify
from app.models.response_model import ApiResponse

def success_response(data, message=None, pagination=None, **kwargs):
    return jsonify(ApiResponse(data=data, pagination=pagination, message=message).__dict__)

def error_response(message, status='error', **kwargs):
    return jsonify(ApiResponse(data=None, message=message, status=status).__dict__), 400
