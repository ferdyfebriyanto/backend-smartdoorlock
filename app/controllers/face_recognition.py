import requests
import os
from deepface import DeepFace
from app.utils import *

def download_image_from_url(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
        
def face_recog_deepface(image1, image2, model, detector):
  # Menentukan path tempat penyimpanan sementara
  image_temp_dir = "image_temp"
  os.makedirs(image_temp_dir, exist_ok=True)
  
  # Mengunduh gambar dari URL dan menyimpannya di folder image_temp
  image1_path = os.path.join(image_temp_dir, "image1.jpg")
  image2_path = os.path.join(image_temp_dir, "image2.jpg")
  download_image_from_url(image1, image1_path)
  download_image_from_url(image2, image2_path)
    
  recog = DeepFace.verify(img1_path=image1_path, img2_path=image2_path, model_name=model, enforce_detection=False, detector_backend=detector)
  
  print(recog)
  
  # Menghapus file gambar sementara
  os.remove(image1_path)
  os.remove(image2_path)
  os.rmdir(image_temp_dir)
  
  return recog