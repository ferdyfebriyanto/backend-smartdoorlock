from flask import request
from app.models.user_model import User
from app.utils import *

def get_users():
    users = User.get_all()
    if users:
        return success_response(users)
    else:
        return error_response("User tidak ada")

    
def create_user():
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    phone = request.json.get('phone', None)

    emailCek = User.get_by_email(email)
    if emailCek:
        return error_response("email sudah ada")

    user = User.create(name, email, password, phone)
    if not user:
        return error_response("gagal membuat akun")
    
    return success_response(user)


def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return success_response(user)
    else:
        return error_response("User tidak ada")


def update_user(user_id):
    print(request.json)
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    phone = request.json.get('phone', None)

    user = User.update(user_id=user_id, name=name, email=email, password=password, phone=phone)
    if user:
        return success_response(user)
    else:
        return error_response("User not found")

def delete_user(user_id):
    user = User.delete_by_id(user_id)
    if user:
        return success_response(user)
    else:
        return error_response("User not found")
