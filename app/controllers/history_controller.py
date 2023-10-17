from flask import request
from app.models.history_model import History
from app.utils import *

def get_histories():
    histories = History.get_all()
        
    return success_response(histories)