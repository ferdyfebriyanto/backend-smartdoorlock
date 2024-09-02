import os


class Config:
    # MongoDB configuration
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_URI', 'mongodb://localhost:26999/smart-door-lock')
        # 'host': os.environ.get('MONGODB_URI', 'mongodb+srv://laudryfadian5:TwpKPpjzsLhXK0tD@cluster0.wvjlfip.mongodb.net/smart-door-lock?retryWrites=true&w=majority')
    }
