import websockets
import base64
from io import BytesIO
from app.helpers.http_client import http_client
from config import Config
import app.services.face_service as FaceService

class WebSocketClient:
    def __init__(self, uri, headers={}):
        self.uri = uri
        self.websocket = None
        self.running = True
        self.headers = headers
        print(f"Websocket uri: {uri}")

    async def connect(self):
        try:
            async with websockets.connect(self.uri, subprotocols=["backend"]) as websocket:
                self.websocket = websocket
                await self.on_connect()
                await self.listen()
        except websockets.ConnectionClosed as e:
            print(f"Connection closed with error: {e}")
        finally:
            await self.on_close()

    async def on_connect(self):
        print("Connected to the WebSocket server.")
        await self.websocket.send("Hello, WebSocket server!")

    async def listen(self):
        while self.running:
            try:
                message = await self.websocket.recv()
                self.process_message(message)
            except websockets.ConnectionClosed as e:
                print(f"Connection closed with error: {e}")
                self.running = False

    async def on_close(self):
        print("Disconnected from the WebSocket server.")

    def process_message(self, message):
        image = base64.b64decode(message)
        image_obj = BytesIO(image)
        files = {'image': ('image.png', image_obj, 'image/png')}
        
        FaceService.process_image(self.websocket, files)

    def stop(self):
        self.running = False

websocket_client = WebSocketClient(uri=Config.WEBSOCKET_URI)