from abc import ABC, abstractmethod
from flash_pymas.entity import EntityInterface


class Agent(EntityInterface):
    def __init__(self, ):
        self.s = "i am an agent"

    


class AgentEvent:
    ...


class AgentEventHandlerInterface(ABC):
    ...
