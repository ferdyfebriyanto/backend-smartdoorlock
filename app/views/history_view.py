from flask import Blueprint
from app.controllers.history_controller import *

history_bp = Blueprint('history', __name__, url_prefix='/histories')

history_bp.route('', methods=['GET'])(get_histories)
history_bp.route('/<history_id>', methods=['GET'])(get_history)