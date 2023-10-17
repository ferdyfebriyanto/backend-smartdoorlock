import time
from flask import request
from app.models.user_model import User
from app.models.category_model import Category
from app.models.absen_model import Absen
from app.models.company_model import Company
from app.models.history_model import History
from app.controllers.face_recognition import *
from app.utils import *

# tambahan untuk base64
import requests
import base64
import pandas as pd

# MQTT
import paho.mqtt.client as mqtt


def absen_check(user_id):
  user = User.get_by_id(user_id)
  if not user:
    return error_response("user tidak ada")
  
  category = Category.get_by_id(user['idCategory'])
  if not category:
    return error_response("user belum punya category")
  
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d') #YYYY-MM-DD
  print(dt)
  print(dateNow)
  timeNow = dt.strftime('%H%M') #HH:MM
  
  toleransiAwalAbsen = 100 #1 jam
  toleransiKeterlambatan = 15 #15 menit
  
  match category['absenCount']:
    case 1:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 1:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      absenTime = int(timeNow)  #batas awal absen
      userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
      absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
      
      if absenTime < userTime:
        return success_response({'message': 'Belum saatnya absen', 'route': "/"})
      
      elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
        return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})
      
      else:
        return success_response({'message': 'Telat absen', 'route': "/"})
      
    case 2:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 2:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      if len(absenNow) == 0:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case 3: #SUDAH BENAR
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 3:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      if len(absenNow) == 0:
        absenTime = int(timeNow) #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/jam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/jam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam3']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam3']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam3"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case 4:
      absenNow = Absen.get_by_id_user_n_datenow(user['id'], dateNow)
      if len(absenNow) == 4:
        return success_response({'message': 'Kamu sudah absen hari ini'})
      
      if len(absenNow) == 0:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam1']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam1']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam1"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 1:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam2']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam2']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam2"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
      
      if len(absenNow) == 2:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam3']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam3']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam3"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
      if len(absenNow) == 3:
        absenTime = int(timeNow)  #batas awal absen
        userTime = int(category['jam4']) - toleransiAwalAbsen #jam absen user
        absenTimeWithToleransi = int(category['jam4']) + toleransiKeterlambatan #batas akhir absen user
        
        if absenTime < userTime:
          return success_response({'message': 'Belum saatnya absen', 'route': "/"})

        elif absenTime >= userTime and absenTime <= absenTimeWithToleransi:
          return success_response({'message': 'Sudah saatnya absen', 'route': "/absenJam4"})

        else:
          return success_response({'message': 'Telat absen', 'route': "/"})
        
    case _:
      return error_response('Terjadi kesalahan, mohon hubungi admin')

def absen(jam): #param jam = jam1/jam2/jam3/jam4
  idUser = request.json['idUser']
  idCompany = request.json['idCompany']
  image = request.json['image']
  lat = request.json['lat']
  long = request.json['long']
  
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  timeNow = dt.strftime('%H%M') #HH:MM
  
  # cek = Absen.get_by_id_user_n_datenow_n_type(idUser, dateNow, jam)
  # if cek[0]:
  #   return error_response("Kamu sudah absen!")
  
  user = User.get_by_id(idUser)
  if not user:
    return error_response("user tidak ada")
  
  faceRecog = face_recog_deepface(image1=user['image'], image2=image, model="Facenet512")
  if not faceRecog:
    return error_response("Face Recognition gagal, harap coba lagi")
  
  absen = Absen.create(idUser=idUser, image=image, approve="Aproved", date=dateNow, idCompany=idCompany, status="Absen Masuk", type=jam, lat=lat, long=long, time=timeNow)
  
  return success_response(absen)

def get_absen_by_id_user(user_id):
  absens = Absen.get_by_id_user(user_id)
  if absens:
    return success_response(absens)
  else:
    return error_response("gagal lihat history")
  
def get_absen_by_id_user_n_date(user_id):
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  
  absens = Absen.get_by_id_user_n_datenow(user_id, dateNow)
  return success_response(absens)
  
def get_user_absen_today(company_id):
  dt = datetime.datetime.now()
  dateNow = dt.strftime('%Y-%m-%d')
  
  absen = Absen.get_by_id_company_n_date(company_id, dateNow)
  if absen:
    for i in range(len(absen)):
      user = User.get_by_id(absen[i]['idUser'])
      if not user:
        return error_response("user tidak ada")

      absen[i]['idUser'] = {'id': str(user['id']), 'name': user['name']}
      
  return success_response(absen)

def get_absen_by_date(date):
  absens = Absen.get_by_datenow(datenow=date)
  if absens:
    for i in range(len(absens)):
      user = User.get_by_id(absens[i]['idUser'])
      company = Company.get_by_id(absens[i]['idCompany'])
      absens[i]['idUser'] = user
      absens[i]['idCompany'] = company
  
  return success_response(absens)

def get_absen_by_date_n_company(company_id, date):
  absens = Absen.get_by_datenow_n_company(company=company_id,datenow=date)
  if absens:
    for i in range(len(absens)):
      user = User.get_by_id(absens[i]['idUser'])
      company = Company.get_by_id(absens[i]['idCompany'])
      absens[i]['idUser'] = user
      absens[i]['idCompany'] = company
  
  return success_response(absens)

def test_deepface():
  image1 = request.json['image']

  user = User.get_all()
  if not user:
    return error_response("user tidak ada")
  
  # Konfigurasi broker MQTT
  broker_address = "test.mosquitto.org"  # Masukkan alamat broker MQTT Anda di sini
  port = 1883  # Port default untuk MQTT
  topic = "inTopic"  # Topik yang akan digunakan untuk mengirim data ke ESP32-CAM

  # Inisialisasi client MQTT
  client = mqtt.Client("PythonClient")  # Beri nama unik untuk klien Anda

  def on_connect(client, userdata, flags, rc):
      if rc == 0:
          print("Terhubung ke broker MQTT")
      else:
          print("Gagal terhubung dengan kode error: " + str(rc))

  def on_publish(client, userdata, mid):
      print("Pesan terpublikasi")

  # Mengatur callback
  client.on_connect = on_connect
  client.on_publish = on_publish

  # Menghubungkan ke broker
  client.connect(broker_address, port)

  # Menunggu koneksi terhubung
  client.loop_start()
  time.sleep(2)
  
  data = []
  for i in range(len(user)):
    result = face_recog_deepface(image1=user[i]['image'], image2=image1, model="ArcFace", detector="mtcnn")
    obj = {
      "verified": result['verified'],
      "distance": result['distance'],
      "threshold": result['threshold'],
      "model": result['model'],
      "detector": result['detector_backend'],
      "similarity_metric": result['similarity_metric'],
      "time": result['time']
    }

    data.append(obj)


    try:
        if result['verified']:
        # if result['verified'] and result['distance'] <= 0.4:
            dt = datetime.datetime.now()
            dateNow = dt.strftime('%Y-%m-%d')
            timeNow = dt.strftime('%H%M')

            # Ambil dua digit pertama sebagai jam
            jam = timeNow[:2]
            
            # Ambil dua digit terakhir sebagai menit
            menit = timeNow[2:]
            
            # Gabungkan kembali dengan format waktu yang sesuai
            waktu_format = f"{jam}:{menit}"

            history = History.create(idUser=user[i]['id'], name=user[i]['name'], date=dateNow, status="Masuk", image=image1, time=waktu_format)
            if not history:
              error_response("gagal absen")

            # Kirim pesan ke ESP32-CAM
            pesan = "1"  # Ganti pesan sesuai kebutuhan Anda
            client.publish(topic, pesan)
            print("Pesan terkirim: " + pesan)
            break
            # time.sleep(2)  # Tunda pengiriman pesan selama 5 detik
        else:
            dt = datetime.datetime.now()
            dateNow = dt.strftime('%Y-%m-%d')
            timeNow = dt.strftime('%H%M')

            # Ambil dua digit pertama sebagai jam
            jam = timeNow[:2]
            
            # Ambil dua digit terakhir sebagai menit
            menit = timeNow[2:]
              
            # Gabungkan kembali dengan format waktu yang sesuai
            waktu_format = f"{jam}:{menit}"

            history = History.create(idUser=user[i]['id'], name=user[i]['name'], date=dateNow, status="Gagal", image=image1, time=waktu_format)
            # Kirim pesan ke ESP32-CAM
            pesan = "0"  # Ganti pesan sesuai kebutuhan Anda
            client.publish(topic, pesan)
            print("Pesan terkirim: " + pesan)
            # time.sleep(2)  # Tunda pengiriman pesan selama 5 detik
    except KeyboardInterrupt:
        pass

  
  # Berhenti dari loop dan putus koneksi
  client.loop_stop()
  client.disconnect()
    
  df = pd.DataFrame(data)
  namaExcel = "hasil_test.xlsx"
  sheetName = 'DataSheet'

  df.to_excel(namaExcel, sheet_name=sheetName, index=False)

  return success_response(data)

def upload_image_to_uploadcare(base64image):
    # Membaca base64image dan mengubahnya menjadi byte object
    image_data = base64.b64decode(base64image)
    
    pub_key = '448aa6eb11abd3614ce5'

    payload = {
        'UPLOADCARE_PUB_KEY': pub_key,
    }

    # Meng-upload image ke uploadcare.com
    upload_url = 'https://upload.uploadcare.com/base/'
    response = requests.post(upload_url, files={'uploaded_file': image_data}, data=payload)

    # Memeriksa apakah pengunggahan berhasil
    if response.status_code == 200:
        # Mendapatkan URL dari response JSON
        uploaded_url = response.json()['file']
        return uploaded_url
    else:
        # Jika terjadi kesalahan, tampilkan pesan error
        print(f"Upload gagal dengan kode status: {response.status_code}")
        return None

