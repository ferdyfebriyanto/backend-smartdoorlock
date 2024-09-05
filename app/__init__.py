from flask import Flask, jsonify
from app.views.user_view import user_bp
from app.views.history_view import history_bp
from app.views.employee_view import employee_bp
from config import Config
from app.database import initialize_db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)

    initialize_db(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(employee_bp)
    
    @app.errorhandler(Exception)
    def handle_error(e):
        # Create a dictionary to hold the error message
        error = {'statusCode': 500, 'errorMessage': str(e)}
    
        # Return a JSON response with the error message
        return jsonify(error), 500

    return app