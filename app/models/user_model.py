from datetime import datetime

from bson import ObjectId
from app.database import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    phone = db.StringField(required=True)
    job = db.StringField(required=True)
    superUser = db.BooleanField(required=True)
    salary = db.IntField(required=True)
    isAbsen = db.BooleanField(required=True)
    jobType = db.StringField(required=True)
    image = db.StringField(required=True)
    verify = db.BooleanField(default=False, required=True)
    idCompany = db.ObjectIdField(required=True, default=lambda: ObjectId())
    idCategory = db.ObjectIdField(default=lambda: ObjectId())
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'job': self.job,
            'superUser': self.superUser,
            'salary': self.salary,
            'isAbsen': self.isAbsen,
            'jobType': self.jobType,
            'image': self.image,
            'verify': self.verify,
            'idCompany': str(self.idCompany),
            'idCategory': str(self.idCategory) if str(self.idCategory) else None
        }

    @staticmethod
    def get_all():
        users = User.objects.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def create(name, email, password, phone, job, superUser, salary, jobType, image, verify, idCompany, isAbsen, idCategory=None):
        user = User(name=name, email=email, password=password, phone=phone, job=job, superUser=superUser, salary=salary, jobType=jobType, image=image, verify=verify, idCompany=idCompany, isAbsen=isAbsen, idCategory=idCategory)
        user.save()
        return user.to_dict()

    @staticmethod
    def update(user_id, name=None, email=None, password=None, phone=None, job=None, superUser=None, salary=None, jobType=None, image=None, verify=None, idCompany=None, isAbsen=None, idCategory=None):
        user = User.objects(id=user_id).first()
        if not user:
            return None
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            user.password = password
        if phone:
            user.phone = phone
        if job:
            user.job = job
        if superUser:
            user.superUser = superUser
        if salary:
            user.salary = salary
        if jobType:
            user.jobType = jobType
        if image:
            user.image = image
        if isAbsen:
            user.isAbsen = isAbsen
        if verify:
            user.verify = verify
        if idCompany:
            user.idCompany = idCompany
        if idCategory:
            user.idCategory = idCategory
        user.isAbsen = isAbsen
        user.save()
        return user.to_dict()

    @staticmethod
    def delete_by_id(id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return user.to_dict()
        except User.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_id(user_id):
        try:
            user = User.objects.get(id=user_id)
            return user.to_dict()
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_by_email(email):
        try:
            user = User.objects.get(email=email)
            return user.to_dict()
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_by_id_company(idCompany):
        try:
            users = User.objects.filter(idCompany=ObjectId(idCompany))
            return [user.to_dict() for user in users]
        except User.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_id_category(idCategory):
        try:
            users = User.objects.filter(idCategory=ObjectId(idCategory))
            return [user.to_dict() for user in users]
        except User.DoesNotExist:
            return None
    