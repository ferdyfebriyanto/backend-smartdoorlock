import requests
import json
from config import Config 

class HttpClient:
    def __init__(self, base_url, headers={}):
        self.base_url = base_url
        self.request = requests.Session()
        self.request.headers.update(headers)

    def post(self, endpoint, data=None, files=None):
        try:
            url = self.base_url + endpoint
            response = self.request.post(url=url, data=data, files=files)
            res = response.json()

            if (response.status_code == 200):
                return res
            
            return None
        except requests.exceptions.RequestException as e:
            print(f"error on request: {e}")
            return None

    def get(self, endpoint):
        try:
            url = self.base_url + endpoint
            response = self.request.get(url)
            res = response.json()

            if (response.status_code == 200):
                return res
            
            return None
        except requests.exceptions.RequestException as e:
            print(f"error on request: {e}")
            return None
        
    def delete(self, endpoint):
        try:
            url = self.base_url + endpoint
            response = self.request.delete(url)
            res = response.json()

            if (response.status_code == 200):
                return res
            
            return None
        except requests.exceptions.RequestException as e:
            print(f"error on request: {e}")
            return None
        
http_client = HttpClient(
    base_url=Config.FACE_RECOG_URL, 
    headers={'e-face-api-key': Config.FACE_RECOG_API_KEY},
    )
