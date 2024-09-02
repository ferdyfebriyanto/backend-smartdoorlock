# app/utils.py

import datetime
from flask import jsonify


def success_response(data):
    response = {
        "status": True,
        "statusCode": 200,
        "timestamp": datetime.datetime.utcnow(),
        "data": data
    }
    return jsonify(response), 200


def error_response(message, status_code=400):
    response = {
        "status": False,
        "statusCode": status_code,
        "timestamp": datetime.datetime.utcnow(),
        "data": None,
        "message": message
    }
    return jsonify(response), status_code
