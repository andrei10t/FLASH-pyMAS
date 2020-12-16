from abc import ABC, abstractmethod


class EntityProxyInterface(EntityInterface):
    @abstractmethod
    def getEntityName(self) -> str:
        pass


class EntityInterface(ABC):
    @abstractmethod
    def addContext(self, context: EntityProxyInterface) -> bool:
        pass

    def __init__(self, name):
        self._name = name
        self._running = False

    def start(self):
        if not self._running:
            self._running = True

    def stop(self):
        if self._running:
            self._running = False

    @property
    def isRunning(self) -> bool:
        return self._running

    @property
    def getName(self) -> str:
        return self._name

    @abstractmethod
    def addContext(self, context: EntityProxyInterface) -> bool:
        pass

    @abstractmethod
    def removeContext(self, context: EntityProxyInterface) -> bool:
        pass

    @abstractmethod
    def addGeneralContext(self, context: EntityProxyInterface) -> bool:
        pass

    @abstractmethod
    def removeGeneralContext(self, context: EntityProxyInterface) -> bool:
        pass

    @abstractmethod
    def asContext(self) -> EntityProxyInterface:
        pass
