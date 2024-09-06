from flask import Blueprint
from app.controllers.auth_controller import *

auth_bp = Blueprint('auth', __name__, url_prefix='/login')

auth_bp.route('', methods=['POST'])(login)