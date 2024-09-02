import asyncio
import threading
import websockets
import base64
from io import BytesIO
from app.helpers.http_client import HttpClient

httpClient = HttpClient(base_url='http://192.168.60.86:9000', headers={'e-face-api-key': 'gAAAAABm1X2NybiW4kOt-urGFUjV4wYrnhyLQ-ZoH6aK2OOab9W0RvRxaIbDaDiPNd_mgs35hiGslB5pMmFEBEtWD3nIJ1eklmPnR0UmnLnNZN2rtkgcgdd4UxRmpUfceIlfLmTrJewdLMpVqDzByATgjb5USdarOzyU71ChXYwfKWHVQQeQp2a80kGGYa3iXEY7OcO1U2mIOaF2ny2mWGTPrqP-Bqe1OdZWAUSKO6vVL1BwYdh8Wc54-OVwmb8iuRw4wT38Th19art-9zGRRS-t1sB3xYksw8REPdFtINtTrsHZr06Aydg_7IGPJ7_gli4P6EBk7b7vwHlcslNhrvio0UJ2Ix383Jkyd_sFcxSnE5MbRBfPt82WNVuQQf2Ds3M19P35x16rxMDRIzU1TWnlt8op3x-DaxAwndgFPnO_VstkmJqhpWLj02chSQtkk0UZMAMsVT5wq2GNUkxKZ4r4ze9Q08ysIV2j41DoBQf-IJ-UH3WJrvubp8VYe4yEURllPU29JCUsbXxlvTDiLIBrTuBQ4y_-9slH3d5nKLuuuwCDgBh386xLPA7i16QdtP4T8eybmu_NOAi8a7LHdkqGBq5FOmk-WkA-BLsr65q6i6LfP1m-KSl5OV_VFVO45lOmgoINHjxTcUnoXeY5vxHkw04yK31f_A=='})


class WebSocketClient:
    def __init__(self, uri, headers={}):
        """
        Initialize the WebSocket client.

        :param uri: The WebSocket server URI.
        :param headers: A dictionary of headers to be included in the connection request.
        """
        self.uri = uri
        self.websocket = None
        self.running = True
        self.headers = headers

    async def connect(self):
        """
        Connect to the WebSocket server with custom headers and manage the connection lifecycle.
        """
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
        """
        Handle actions to perform when the connection is established.
        """
        print("Connected to the WebSocket server.")
        await self.websocket.send("Hello, WebSocket server!")

    async def listen(self):
        """
        Listen for incoming messages from the server.
        """
        while self.running:
            try:
                message = await self.websocket.recv()
                self.process_message(message)
            except websockets.ConnectionClosed as e:
                print(f"Connection closed with error: {e}")
                self.running = False

    async def on_close(self):
        """
        Handle actions to perform when the connection is closed.
        """
        print("Disconnected from the WebSocket server.")

    def process_message(self, message):
        """
        Process incoming messages.
        """
        image = base64.b64decode(message)
        image_obj = BytesIO(image)
        files = {'image': ('image.png', image_obj, 'image/png')}
        recognize_face_res = httpClient.post('/face_recognition', files=files)
        print(recognize_face_res)

    def stop(self):
        """
        Stop the WebSocket client.
        """
        self.running = False
