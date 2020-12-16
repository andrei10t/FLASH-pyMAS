from abc import ABC, abstractmethod
from entity import EntityInterface


class ConfigurableEntityInterface(EntityInterface, Configurable):
    @abstractmethod
    def configure(self, config: dict) -> bool:
        pass
