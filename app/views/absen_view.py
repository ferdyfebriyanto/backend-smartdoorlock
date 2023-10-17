from flask import Blueprint
from app.controllers.absen_controller import *

absen_bp = Blueprint('absen', __name__, url_prefix='/absen')

absen_bp.route('/<string:date>', methods=['GET'])(get_absen_by_date)
absen_bp.route('/<string:company_id>/<string:date>', methods=['GET'])(get_absen_by_date_n_company)
absen_bp.route('/cek/<string:user_id>', methods=['GET'])(absen_check)
absen_bp.route('/<string:jam>', methods=['POST'])(absen)
absen_bp.route('/history/<string:user_id>', methods=['GET'])(get_absen_by_id_user)
absen_bp.route('/usertoday/<string:user_id>', methods=['GET'])(get_absen_by_id_user_n_date)
absen_bp.route('/today/<string:company_id>', methods=['GET'])(get_user_absen_today)
absen_bp.route('/uploadcare/<string:base64image>', methods=['GET'])(upload_image_to_uploadcare)
absen_bp.route('/testferdy', methods=['POST'])(test_deepface)
