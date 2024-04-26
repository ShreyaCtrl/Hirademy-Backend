from flask import Blueprint, jsonify

error_bp = Blueprint('error', __name__)

@error_bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({
        'message': 'Resource not found',
        'status': 404,
        'statusText': 'Not Found',
        'mime-type': 'application/json'
    }), 404

@error_bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({
        'message': 'Internal Server Error',
        'status': 500,
        'statusText': 'Internal Server Error',
        'mime-type': 'application/json'
    }), 500
