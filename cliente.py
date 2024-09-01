import asyncio
import websockets



async def communicate():
    uri = "ws://childlike-flicker-hubcap.glitch.me/socket"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hola desde Python! ... funciona")
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

# Ejecutar la comunicación
asyncio.get_event_loop().run_until_complete(communicate())
