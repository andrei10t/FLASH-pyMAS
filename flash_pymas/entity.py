from abc import ABC, abstractmethod


class EntityProxyInterface:
    @abstractmethod
    def getEntityName(self) -> str:
        pass


class EntityInterface(ABC):
    # def __init__(self, name=None):
    #     self._name = name
    #     self._running = False
    #     self.context = []

    def start(self):
        if not self._running:
            self._running = True

    def stop(self):
        if self._running:
            self._running = False

    @property
    def registered_entities(self) -> dict:
        return self._registered_entities

    @property
    def isRunning(self) -> bool:
        return self._running

    @property
    def getName(self) -> str:
        return self._name

    # @abstractmethod
    # def addContext(self, context: EntityProxyInterface) -> bool:
    #     pass

    # @abstractmethod
    # def removeContext(self, context: EntityProxyInterface) -> bool:
    #     pass

    # @abstractmethod
    # def addGeneralContext(self, context: EntityProxyInterface) -> bool:
    #     pass

    # @abstractmethod
    # def removeGeneralContext(self, context: EntityProxyInterface) -> bool:
    #     pass

    # @abstractmethod
    # def asContext(self) -> EntityProxyInterface:
    #     pass
