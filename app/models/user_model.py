from datetime import datetime
from app.database import db

class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    phone = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def get_all():
        users = User.objects.all()
        return [user.to_dict() for user in users]

    @staticmethod
    def create(name, email, password, phone):
        user = User(name=name, email=email, password=password, phone=phone)
        user.save()
        return user.to_dict()

    @staticmethod
    def update(user_id, name=None, email=None, password=None, phone=None):
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
    