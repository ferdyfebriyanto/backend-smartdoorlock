from app.models.employee_model import Employee
from app.models.history_model import History
from app.helpers.http_client import http_client

async def register_face(data, files):
  res  = http_client.post('/face_registration', data, files)
  if res is None:
      Employee.update(data['identifier'], face_id=None, face_status='Failed')
  else:
    if res['status_code'] == 200:
      Employee.update(data['identifier'], face_id=res['result'], face_status='Registered')
    else:
      Employee.update(data['identifier'], face_id=None, face_status='Failed')

async def delete_face(face_id):
  res = http_client.delete(f'/delete_face/{face_id}')
  if res is None:
      return None
  if res['status_code'] == 200:
    return True
  else:
    return False

def recognize_face(files):
  res = http_client.post('/face_recognition', files=files)
  print(f'Response: {res}')
  if res is None:
      return None
  
  result = res['result']
  if res['status_code'] == 200 and result is not None:
    user = result['user']
    verified = result['verified']

    response = {
      'verified': verified,
      'employee_id': user['_id'],   
    }

    return response
  else:
    return None

async def process_image(websocket, files):
  res = recognize_face(files)
  
  if res is None:
      History.create(status=False, message='Unknown user tried to access the system')
      await websocket.send("false")
      return
  
  if res['verified']:
    employee = Employee.get_by_face_id(res['employee_id'])
    if employee is not None:
      History.create(status=True, message='successfully accessed the system', user=employee['id'])
      await websocket.send("true")
    else:
      History.create(status=False, message='Unknown user tried to access the system')
      await websocket.send("false")
  else:
    History.create(status=False, message='Unknown user tried to access the system')
    await websocket.send("false")