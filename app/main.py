from fastapi import FastAPI
from routers.websocket import websocket_router

app = FastAPI()

app.include_router(websocket_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)