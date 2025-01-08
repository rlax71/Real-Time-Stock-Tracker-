from fastapi import WebSocket
import asyncio

async def stock_updates(websocket: WebSocket, ticker: str):
    await websocket.accept()
    while True:
        # Simulate stock price updates (replace this with actual API integration)
        price = await fetch_stock_price(ticker)
        await websocket.send_json({"ticker": ticker, "price": price})
        await asyncio.sleep(1)

async def fetch_stock_price(ticker: str):
    # Replace this with an API call to get live stock prices
    return 100 + (hash(ticker) % 10)  # Mock price