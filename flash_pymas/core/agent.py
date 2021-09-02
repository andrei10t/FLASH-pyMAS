from abc import ABC, abstractmethod

from flash_pymas.entity import EntityInterface


class Agent(EntityInterface):
    def __init__(self, name=None):
        self._running = False
        self._name = name
        self._registered_entities = dict()
        self._entity_order = []


class AgentEvent:
    ...


class AgentEventHandlerInterface(ABC):
    ...
