from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.websocket import stock_updates
from app.db import setup_db

app = FastAPI()

# WebSocket endpoint for real-time stock updates
@app.websocket("/ws/{ticker}")
async def websocket_endpoint(websocket: WebSocket, ticker: str):
    try:
        # Log connection start
        print(f"Client connected to WebSocket for ticker: {ticker}")
        await stock_updates(websocket, ticker)
    except WebSocketDisconnect:
        # Handle disconnection gracefully
        print(f"Client disconnected from WebSocket for ticker: {ticker}")
    except Exception as e:
        # Log unexpected errors
        print(f"Error in WebSocket connection: {e}")

# Run setup tasks when the app starts
@app.on_event("startup")
async def startup():
    try:
        print("Running database setup...")
        setup_db()
        print("Database setup completed.")
    except Exception as e:
        # Log any startup errors
        print(f"Error during startup: {e}")