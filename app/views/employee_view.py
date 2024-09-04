from flask import Blueprint
from app.controllers.employee_controller import *

employee_bp = Blueprint('employee', __name__, url_prefix='/employees')

employee_bp.route('', methods=['GET'])(get_employees)
employee_bp.route('', methods=['POST'])(create_employee)
employee_bp.route('/<string:employee_id>', methods=['GET'])(get_employee)
employee_bp.route('/<string:employee_id>', methods=['PUT'])(update_employee)
employee_bp.route('/<string:employee_id>', methods=['DELETE'])(delete_employee)