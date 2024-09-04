from flask import request
from app.models.employee_model import Employee
from app.utils import *
from io import BytesIO
import requests
import asyncio
from app.services.face_service import FaceService

def get_employees():
    employees = Employee.get_all()
    if employees:
        return success_response(employees)
    else:
        return error_response("Data karyawan tidak ada")
    
def create_employee():
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    phone = request.json.get('phone', None)
    job = request.json.get('job', None)
    salary = request.json.get('salary', None)
    image = request.json.get('image', None)

    emailCek = Employee.get_by_email(email)
    if emailCek:
        return error_response("email sudah ada")

    employee = Employee.create(name=name, email=email, phone=phone, job=job, salary=salary, image=image)
    if not employee:
        return error_response("gagal menambahkan data karyawan")

    img = requests.get(employee['image']).content
    image = BytesIO(img)

    data = {
        'identifier': employee['id'],
        'real_name': employee['name'],
    }

    files = {'image': ('image.png', image, 'image/png')}

    asyncio.run(FaceService.register_face(data, files))      
    return success_response(employee)

def get_employee(employee_id):
    employee = Employee.get_by_id(employee_id)
    if employee:
        return success_response(employee)
    else:
        return error_response("Data karyawan tidak ada")

def update_employee(employee_id):
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    phone = request.json.get('phone', None)
    job = request.json.get('job', None)
    salary = request.json.get('salary', None)
    image = request.json.get('image', None)

    employee = Employee.update(employee_id, name=name, email=email, phone=phone, job=job, salary=salary, image=image)
    if employee:
        return success_response(employee)
    else:
        return error_response("Data karyawan tidak ada")

def delete_employee(employee_id):
    employee = Employee.delete_by_id(employee_id)
    if employee:
        return success_response(employee)
    else:
        return error_response("Data karyawan tidak ada")