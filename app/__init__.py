from flask import Flask, jsonify
from app.views.user_view import user_bp
from app.views.company_view import company_bp
from app.views.auth_view import auth_bp
from app.views.setting_view import setting_bp
from app.views.config_view import config_bp
from app.views.category_view import category_bp
from app.views.absen_view import absen_bp
from app.views.history_view import history_bp
from app.views.unregister_face_view import unregister_bp
from config import Config
from app.database import initialize_db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)

    initialize_db(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(setting_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(absen_bp)
    app.register_blueprint(unregister_bp)
    app.register_blueprint(history_bp)
    
    @app.errorhandler(Exception)
    def handle_error(e):
        # Create a dictionary to hold the error message
        error = {'statusCode': 500, 'errorMessage': str(e)}
    
        # Return a JSON response with the error message
        return jsonify(error), 500

    return app