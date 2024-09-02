from flask import request
from app.models.user_model import User
from app.models.company_model import Company
from app.models.category_model import Category
from app.utils import *
from io import BytesIO
import requests
from app.helpers.http_client import HttpClient

httpClient = HttpClient(base_url='http://192.168.60.86:9000', headers={'e-face-api-key': 'gAAAAABm1X2NybiW4kOt-urGFUjV4wYrnhyLQ-ZoH6aK2OOab9W0RvRxaIbDaDiPNd_mgs35hiGslB5pMmFEBEtWD3nIJ1eklmPnR0UmnLnNZN2rtkgcgdd4UxRmpUfceIlfLmTrJewdLMpVqDzByATgjb5USdarOzyU71ChXYwfKWHVQQeQp2a80kGGYa3iXEY7OcO1U2mIOaF2ny2mWGTPrqP-Bqe1OdZWAUSKO6vVL1BwYdh8Wc54-OVwmb8iuRw4wT38Th19art-9zGRRS-t1sB3xYksw8REPdFtINtTrsHZr06Aydg_7IGPJ7_gli4P6EBk7b7vwHlcslNhrvio0UJ2Ix383Jkyd_sFcxSnE5MbRBfPt82WNVuQQf2Ds3M19P35x16rxMDRIzU1TWnlt8op3x-DaxAwndgFPnO_VstkmJqhpWLj02chSQtkk0UZMAMsVT5wq2GNUkxKZ4r4ze9Q08ysIV2j41DoBQf-IJ-UH3WJrvubp8VYe4yEURllPU29JCUsbXxlvTDiLIBrTuBQ4y_-9slH3d5nKLuuuwCDgBh386xLPA7i16QdtP4T8eybmu_NOAi8a7LHdkqGBq5FOmk-WkA-BLsr65q6i6LfP1m-KSl5OV_VFVO45lOmgoINHjxTcUnoXeY5vxHkw04yK31f_A=='})


def get_users():
    users = User.get_all()
    if users:
        for i in range(len(users)):
            company = Company.get_by_id(users[i]['idCompany'])
            users[i]['idCompany'] = company
    # print(users)
    return success_response(users)


def create_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    job = request.json['job']
    superUser = request.json['superUser']
    salary = request.json['salary']
    isAbsen = request.json['isAbsen']
    jobType = request.json['jobType']
    idCompany = request.json['idCompany']
    image = request.json['image']
    verify = request.json['verify']
    idCategory = request.json['idCategory']

    emailCek = User.get_by_email(email)
    if emailCek:
        return error_response("email sudah ada")

    user = User.create(name, email, password, phone, job, superUser,
                       salary, jobType, image, verify, idCompany, isAbsen, idCategory)
    if not user:
        return error_response("gagal membuat akun")

    print(user)

    # data = {
    #     'identifier': user['id'],
    #     'real_name': user['name'],
    # }

    img = requests.get(user['image']).content
    image = BytesIO(img)

    data = {
        'identifier': user['id'],
        'real_name': user['name'],
    }

    files = {'image': ('image.png', image, 'image/png')}

    register_face_res = httpClient.post('/face_registration', data, files)
    print(register_face_res)
    return success_response(user)


def get_user(user_id):
    user = User.get_by_id(user_id)
    if user:
        return success_response(user)
    else:
        return error_response("User tidak ada")


def update_user(user_id):
    print(request.json)
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    job = request.json['job']
    superUser = request.json['superUser']
    salary = request.json['salary']
    isAbsen = request.json['isAbsen']
    jobType = request.json['jobType']
    idCompany = request.json['idCompany']
    image = request.json['image']

    user = User.update(user_id=user_id, name=name, email=email, idCompany=idCompany, isAbsen=isAbsen, job=job,
                       jobType=jobType, password=password, phone=phone, salary=salary, superUser=superUser, image=image)
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


def get_user_by_id_company(company_id):
    # user = User.get_by_id_company(company_id)
    # print(user)
    # if user:
    #     return success_response(user)
    # else:
    #     return error_response("User tidak ada")
    user = User.get_by_id_company(company_id)
    if user:
        for i in range(len(user)):
            company = Company.get_by_id(user[i]['idCompany'])
            user[i]['idCompany'] = company
    return success_response(user)


def login_mobile():
    email = request.json['email']
    password = request.json['password']

    emailCek = User.get_by_email(email)
    if not emailCek:
        return error_response("Email salah")

    if emailCek['password'] != password:
        return error_response("Password salah")

    category = Category.get_by_id(emailCek['idCategory'])
    company = Company.get_by_id(emailCek['idCompany'])
    emailCek['category'] = category['name']
    emailCek['company'] = company['name']

    return success_response(emailCek)
