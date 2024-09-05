from app import create_app
import asyncio
import threading
from app.helpers.websockets import websocket_client

app = create_app()

async def connect_to_websocket():
    await websocket_client.connect()


def run_websocket():
    asyncio.run(connect_to_websocket())


if __name__ == '__main__':
    thread = threading.Thread(target=run_websocket, daemon=True)
    thread.start()

    app.run(debug=True, host='0.0.0.0')
