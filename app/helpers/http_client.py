import requests


class HttpClient:
    def __init__(self, base_url, headers={}):
        self.base_url = base_url
        self.request = requests.Session()
        self.request.headers.update(headers)

    def post(self, endpoint, data=None, files=None):
        try:
            url = self.base_url + endpoint
            print(f"url: {url}")
            response = self.request.post(url=url, files=files)
            response.raise_for_status()
            print(f"response: {response}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"error on request: {e}")
            return None

    def get(self, endpoint):
        try:
            url = self.base_url + endpoint
            self.request.request("GET", url)
            return self.request.getresponse()
        except requests.exceptions.RequestException as e:
            print(f"error on request: {e}")
            return None
