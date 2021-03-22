from abc import ABC, abstractmethod


class Agent:
    def __init__(self, name):
        print("i am agent "+name)

    def funct(self):
        return self.s


class AgentEvent:
    ...


class AgentEventHandlerInterface(ABC):
    ...
