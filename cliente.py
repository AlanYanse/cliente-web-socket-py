import asyncio
import websockets



async def communicate():
    uri = "ws://childlike-flicker-hubcap.glitch.me/socket"
    async with websockets.connect(uri) as websocket:
        #await websocket.send("Hola desde Python! ... funciona")
        #response = await websocket.recv()
        #print(f"Respuesta del servidor: {response}")
        print("Conectado al servidor.")
        
        # Un bucle para enviar y recibir mensajes continuamente
        while True:
            message = input("Tú: ")  # Entrada del usuario
            if message.lower() == "salir":  # Permitir al usuario salir del chat
                print("Desconectando...")
                break
            await websocket.send(message)
            
            response = await websocket.recv()
            print(f"Servidor: {response}")

# Ejecutar la comunicación
asyncio.get_event_loop().run_until_complete(communicate())
