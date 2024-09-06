from flask import request
from app.models.user_model import User
from app.utils import *
import app.helpers.encryptor as Encryptor

def login():
  email = request.json.get('email', None)
  password = request.json.get('password', None)
  
  user = User.get_by_email(email)
  if not user:
    return error_response("email salah")
  
  if Encryptor.check_password(password, user['password']) == False:
    return error_response("password salah")
  
  return success_response(user)
