#!/usr/bin/python3.8

# WSS (WS over TLS) client example, with a self-signed certificate

import asyncio
import pathlib
import pickle
import ssl

import websockets

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
# localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
# ssl_context.load_verify_locations(localhost_pem)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
path_cert = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_verify_locations(path_cert)


class Message:
    def __init__(self, source, dest=None, content=None):
        self._source = source
        self._dest = dest
        self._content = content


async def hello():
    uri = "wss://localhost:8765"
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        message = Message("b")
        await websocket.send(pickle.dumps(message))
        greeting = await websocket.recv()
        greeting = await websocket.recv()
        print(f"received: {greeting}")


asyncio.get_event_loop().run_until_complete(hello())
