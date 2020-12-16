from abc import ABC, abstractmethod
from entity import EntityInterface


class EntityProxyInterface(EntityInterface):
    @abstractmethod
    def getEntityName(self) -> str:
        pass
