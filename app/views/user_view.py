from flask import Blueprint
from app.controllers.user_controller import *

user_bp = Blueprint('user', __name__, url_prefix='/users')

user_bp.route('', methods=['GET'])(get_users)
user_bp.route('', methods=['POST'])(create_user)
user_bp.route('/<string:user_id>', methods=['GET'])(get_user)
user_bp.route('/<string:user_id>', methods=['PUT'])(update_user)
user_bp.route('/<string:user_id>', methods=['DELETE'])(delete_user)