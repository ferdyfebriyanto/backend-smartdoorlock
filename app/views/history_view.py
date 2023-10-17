from flask import Blueprint
from app.controllers.history_controller import *

history_bp = Blueprint('history', __name__, url_prefix='/history')

history_bp.route('', methods=['GET'])(get_histories)