from datetime import datetime
from app.database import db
from bson import ObjectId

class History(db.Document):
    idUser = db.ObjectIdField(required=True, default=lambda: ObjectId())
    name = db.StringField(required=True)
    status = db.StringField(required=True)
    date = db.StringField(required=True)
    time = db.StringField(required=True)
    image = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'idUser': str(self.idUser),
            'name': self.name,
            'status': self.status,
            'date': self.date,
            'time': self.time,
            'image': self.image,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def get_all():
        histories = History.objects.all()
        return [history.to_dict() for history in histories]

    @staticmethod
    def create(idUser, name, status, date, time, image):
        history = History(idUser=idUser, name=name, status=status, date=date, time=time, image=image)
        history.save()
        return history.to_dict()

    @staticmethod
    def update(history_id, idUser=None, name=None, status=None, date=None, time=None, image=None):
        history = History.objects(id=history_id).first()
        if not history:
            return None
        if idUser:
            history.idUser = idUser
        if name:
            history.name = name
        if status:
            history.status = status
        if date:
            history.date = date
        if time:
            history.time = time
        if image:
            history.image = image
        history.save()
        return history.to_dict()

    @staticmethod
    def delete(history_id):
        history = History.objects(id=history_id).first()
        if not history:
            return None
        history.delete()
        return history.to_dict()
    
    @staticmethod
    def get_by_id(history_id):
        try:
            history = History.objects(id=history_id).first()
            return history.to_dict()
        except History.DoesNotExist:
            return None
        
    