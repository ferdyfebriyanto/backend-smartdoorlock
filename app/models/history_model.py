from datetime import datetime
from app.database import db

class History(db.Document):
    user = db.ObjectIdField(required=False, default=None)
    status = db.BooleanField(required=True)
    message = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'user': str(self.user),
            'status': self.status,
            'message': self.message,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def get_all():
        histories = History.objects.all()
        return [history.to_dict() for history in histories]

    @staticmethod
    def create(user=None, status=None, message=None):
        history = History(user=user, status=status, message=message)
        history.save()
        return history.to_dict()

    @staticmethod
    def update(history_id, user, status, message):
        history = History.objects(id=history_id).first()
        if not history:
            return None
        if user:
            history.user = user
        if status:
            history.status = status
        if message:
            history.message = message

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
        
    