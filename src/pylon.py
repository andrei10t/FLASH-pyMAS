from abc import ABC, abstractmethod


class EntityProxy(ABC):
    @abstractmethod
    def getEntityName(self):
        pass
