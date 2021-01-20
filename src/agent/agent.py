from abc import ABC, abstractmethod


class Agent:
    def __init__(self):
        self.s = "i am an agent"

    def funct(self):
        return self.s


class AgentEvent:
    ...


class AgentEventHandlerInterface(ABC):
    ...
