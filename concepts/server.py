#!/usr/bin/python3.8

import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
path_cert = pathlib.Path(__file__).with_name("cert.pem")
path_key = pathlib.Path(__file__).with_name("key.pem")
ssl_context.load_cert_chain(path_cert, keyfile=path_key)

print("Listening for connection...")
# start_server = websockets.serve(handler, HOSTNAME, PORT, ssl=ssl_context)

start_server = websockets.serve(
    hello, "localhost", 8765, ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()