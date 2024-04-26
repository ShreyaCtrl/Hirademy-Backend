from flask import Blueprint

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

from .employee_routes import *
from .error_routes import *