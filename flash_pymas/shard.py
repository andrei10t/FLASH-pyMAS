import asyncio
import pathlib
import ssl
from abc import ABC, abstractmethod
from enum import Enum

import websockets
from agent.agent import AgentEvent
from agent.agentWave import Message
from entity.configurableEntity import ConfigurableEntityInterface
from entity.entity import EntityProxyInterface

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
path_cert = pathlib.Path(__file__).with_name("cert.pem")
ssl_context.load_verify_locations(path_cert)


class AgentShardDesignation(Enum):
    MESSAGING = "message"
    IO = "io"
    GUI = "gui"
    MONITORING = "monitorinig"
    CONTROL = "control"
    KNOWLEDGE = "knowledge"


class AgentShardInterface(ConfigurableEntityInterface):
    @abstractmethod
    def getShardDesignation(self) -> AgentShardDesignation:
        pass

    @abstractmethod
    def signalAgentEvent(self, event: AgentEvent):
        pass


class ShardContainerInterface(EntityProxyInterface):
    @abstractmethod
    def postAgentEvent(self, event: AgentEvent):
        pass

    @abstractmethod
    def getAgentShard(self, designation: AgentShardDesignation) -> AgentShardInterface:
        pass


class Shard(EntityInterface):
    def __init__(self, designation: str, name=None):
        self._running = False
        self._name = name
        self._registered_entities = dict()
        self._entity_order = []
        self._designation = AgentShardDesignation(designation)

    @property
    def designation(self):
        return self._designation

    async def _hello(self):
        uri = "wss://localhost:8765"
        async with websockets.connect(uri, ssl=ssl_context) as websocket:
            write_something = input("write to someone dear:")
            message = Message("a", "b", write_something)
            await websocket.send(pickle.dumps(message))
            greeting = await websocket.recv()
            # print(f"< {pickle.loads(greeting)}")
            print(f"received: {greeting}")

    async def _knows(self):
        uri = "wss://localhost:8765"
        async with websockets.connect(uri, ssl=ssl_context) as websocket:
            message = Message("b")
            await websocket.send(pickle.dumps(message))
            greeting = await websocket.recv()
            greeting = await websocket.recv()
            print(f"I know how to reverse: {greeting[::-1]}")

    def talk(self):
        asyncio.get_event_loop().run_until_complete(self._hello())

    def reverse(self):
        asyncio.get_event_loop().run_until_complete(self._reverse())
