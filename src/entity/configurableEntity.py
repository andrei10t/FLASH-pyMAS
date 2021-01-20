from abc import ABC, abstractmethod
from entity.entity import EntityInterface


class ConfigurableEntityInterface(EntityInterface):
    @abstractmethod
    def configure(self, config: dict) -> bool:
        pass
