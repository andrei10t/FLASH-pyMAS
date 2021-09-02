#!/usr/bin/python3.8

import asyncio
import pathlib
import pickle
import ssl

import websockets


class Message:
    def __init__(self, source, dest=None, content=None):
        self._source = source
        self._dest = dest
        self._content = content


connections = []
deliveries = []
messages = []
lm = []


async def hello(websocket, path):
    new_conn = await websocket.recv()
    message_obj = pickle.loads(new_conn)
    await websocket.send(f"hello {message_obj._source}")
    print(f"new connection from {message_obj._source}")
    if messages:
        for msg in messages:
            if msg._dest is message_obj._source:
                await websocket.send(msg._content)
                print(f"sent message to {message_obj._source}")
    messages.append(message_obj)


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
path_cert = pathlib.Path(__file__).with_name("cert.pem")
path_key = pathlib.Path(__file__).with_name("key.pem")
ssl_context.load_cert_chain(path_cert, keyfile=path_key)

print("Listening for connection...")
# start_server = websockets.serve(handler, HOSTNAME, PORT, ssl=ssl_context)

start_server = websockets.serve(hello, "localhost", 8765, ssl=ssl_context)
# hello is a shard
# localhost e by default
# 8765 portul e argument la pylon

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
