import asyncio
import websockets

async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}/chat") as ws:
        await ws.send(message)
        await ws.recv()

loop = asyncio.run(produce(message='{"msg": "Time for a little chat. "}', host="localhost", port=6980))
