from abc import ABC, abstractmethod


class Configurable(ABC):
    @abstractmethod
    def makeDefaults(self):
        pass

    @abstractmethod
    def lock(self) -> dict:
        pass

    @abstractmethod
    def build(self) -> dict:
        pass

    @abstractmethod
    def ensureLocked(self):
        pass
