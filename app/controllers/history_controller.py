from flask import request
from app.models.history_model import History
from app.models.employee_model import Employee
from app.utils import *

def get_histories():
    histories = History.get_all()
    data = []
    if histories:
        for history in histories:
            hist = {
                'id': history['id'],
                'status': history['status'],
                'message': history['message'],
                'created_at': history['created_at']
            }

            if history['user'] is not '':
                print(history['user'])
                user = Employee.get_by_id(history['user'])
                if user:
                    hist['user'] = {
                        'id': user['id'],
                        'name': user['name'],
                        'email': user['email'],
                        'phone': user['phone'],
                        'job': user['job'],
                    }    
                
            data.append(hist)
        return success_response(data)
    else:
        return error_response("Data history tidak ada")
    
def get_history(history_id):
    history = History.get_by_id(history_id)
    if history:
        hist = {
                'id': history['id'],
                'status': history['status'],
                'message': history['message'],
                'created_at': history['created_at']
            }

        if history['user'] is not '':
            user = Employee.get_by_id(history['user'])
            if user:
                hist['user'] = {
                    'id': user['id'],
                    'name': user['name'],
                    'email': user['email'],
                    'phone': user['phone'],
                    'job': user['job'],
                }    

        return success_response(hist)
    else:
        return error_response("Data history tidak ada")