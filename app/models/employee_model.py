from datetime import datetime
from app.database import db
from enum import Enum

class Status(Enum):
    REGISTERING = 'Registering'
    FAILED = 'Failed'
    REGISTERED = 'Registered'

class Employee(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    phone = db.StringField(required=True)
    job = db.StringField(required=True)
    salary = db.IntField(required=True)
    image = db.StringField(required=True)
    face_status = db.EnumField(Status, default=Status.REGISTERING)
    face_id = db.StringField()
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'job': self.job,
            'salary': self.salary,
            'image': self.image,
            'face_status': self.face_status,
            'face_id': self.face_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def get_all():
        employees = Employee.objects.all()
        return [employee.to_dict() for employee in employees]

    @staticmethod
    def create(name, email, phone, job, salary, image):
        employee = Employee(name=name, email=email, phone=phone, job=job, salary=salary, image=image)
        employee.save()
        return employee.to_dict()

    @staticmethod
    def update(user_id, name=None, email=None, phone=None, job=None, salary=None, image=None):
        employee = Employee.objects(id=user_id).first()
        if not employee:
            return None
        if name:
            employee.name = name
        if email:
            employee.email = email
        if phone:
            employee.phone = phone
        if job:
            employee.job = job
        if salary:
            employee.salary = salary
        if image:
            employee.image = image

        employee.save()
        return employee.to_dict()

    @staticmethod
    def delete_by_id(id):
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return employee.to_dict()
        except Employee.DoesNotExist:
            return None
    
    @staticmethod
    def get_by_id(user_id):
        try:
            employee =Employee.objects.get(id=user_id)
            return employee.to_dict()
        except Employee.DoesNotExist:
            return None
        
    @staticmethod
    def get_by_email(email):
        try:
            employee = Employee.objects.get(email=email)
            return employee.to_dict()
        except Employee.DoesNotExist:
            return None
    