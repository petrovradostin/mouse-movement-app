from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse
import json
from services import camera_service
from database import Database

websocket_router = APIRouter()

# HTML template for the front end
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Mouse Tracker</title>
    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        document.onmousemove = function(event) {
            ws.send(JSON.stringify({ type: 'mouse_movement', x: event.clientX, y: event.clientY }));
        };

        document.onmousedown = function(event) {
            if (event.button === 0) {
                ws.send(JSON.stringify({ type: 'mouse_click' }));
            }
        };
    </script>
</head>
<body></body>
</html>
"""

@websocket_router.get("/")
async def get():
    return HTMLResponse(html)

@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    state = {"x": 0, "y": 0}
    db = Database()

    while True:
        data = await websocket.receive_text()
        message = json.loads(data)
        if message["type"] == "mouse_movement":
            state["x"] = message['x']
            state["y"] = message['y']
            print(f'Mouse moved to ({state["x"]}, {state["y"]})')
        elif message["type"] == "mouse_click":
            image_path = camera_service.capture_image()
            if image_path:
                db.save_mouse_data(state["x"], state["y"], image_path)
                print(f'Image saved at {image_path}')
