from app.models.employee_model import Employee
from app.models.history_model import History
from app.helpers.http_client import http_client

class FaceService:
    async def register_face(data, files):
      res  = http_client.post('/face_registration', data, files)
      print(f"Response: {res}")
      if res is None:
          Employee.update(data['identifier'], face_id=None, face_status='Failed')

      Employee.update(data['identifier'], face_id='11111', face_status='Registered')

    def recognize_face(files):
      res = http_client.post('/face_recognition', files=files)
      if res is None:
          return None
      
      response = {
        'face_id': res['face_id'],
        'confidence': res['confidence'],
        'status': res['status']
      }

      return response
    
    def process_image(self, websocket, files):
      res = self.recognize_face(files)
      
      if res is None:
          # create history
          print("Error on face recognition")
          websocket.send("false")
          return
      
      print(res)
      # if res['status'] == 'success'
      # do some stuff like checking the verified status also get the recognized user
      # create history
      websocket.send("true")