from abc import ABC, abstractmethod


class EntityProxy(ABC):
    @abstractmethod
    def getEntityName(self):
        pass

class Pylon(EntityInterface):
    def __init__(self, name=None):
        # self._running = False
        # self._name = name
        # self._registered_entities = dict()
        # self._entity_order = []
        self._services = set()

