import asyncio
import pathlib
import ssl
from abc import ABC, abstractmethod

import websockets

from flash_pymas.agent.agentWave import Message


class EntityProxy(ABC):
    @abstractmethod
    def getEntityName(self):
        pass


connections = []
deliveries = []
messages = []
lm = []


class Pylon(EntityInterface):
    def __init__(self, name=None):
        # self._running = False
        # self._name = name
        # self._registered_entities = dict()
        # self._entity_order = []
        self._services = set()

    async def hello(self, websocket, path):
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

    def startserver(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        path_cert = pathlib.Path(__file__).with_name("cert.pem")
        path_key = pathlib.Path(__file__).with_name("key.pem")
        ssl_context.load_cert_chain(path_cert, keyfile=path_key)
        print("Listening for connection...")
        start_server = websockets.serve(self.hello, "localhost", 8765, ssl=ssl_context)
