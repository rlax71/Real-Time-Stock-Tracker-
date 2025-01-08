from fastapi import FastAPI, WebSocket
from app.websocket import stock_updates
from app.db import setup_db

app = FastAPI()

# WebSocket endpoint for real-time stock updates
@app.websocket("/ws/{ticker}")
async def websocket_endpoint(websocket: WebSocket, ticker: str):
    await stock_updates(websocket, ticker)

# Run setup tasks when the app starts
@app.on_event("startup")
async def startup():
    setup_db()