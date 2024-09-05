import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')


class Config:
    # MongoDB configuration
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_URI', 'mongodb://localhost:27008/smart-door-lock'),
        # 'host': os.environ.getenv('MONGODB_URI', 'mongodb+srv://laudryfadian5:TwpKPpjzsLhXK0tD@cluster0.wvjlfip.mongodb.net/smart-door-lock?retryWrites=true&w=majority')
    }
    FACE_RECOG_API_KEY = os.getenv('FACE_RECOG_API_KEY', '')
    FACE_RECOG_URL =  os.getenv('FACE_RECOG_URL', 'http://localhost')
    WEBSOCKET_URI = os.getenv('WEBSOCKET_URI', 'ws://localhost:3000')
