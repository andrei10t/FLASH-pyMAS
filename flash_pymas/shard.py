from abc import ABC, abstractmethod
from enum import Enum

from agent.agent import AgentEvent
from entity.configurableEntity import ConfigurableEntityInterface
from entity.entity import EntityProxyInterface


class AgentShardDesignation(Enum):
    MESSAGING = "MESSAGING"
    IO = "IO"
    GUI = "GUI"
    MONITORING = "MONITORING"
    CONTROL = "CONTROL"


class AgentShardInterface(ConfigurableEntityInterface):
    @abstractmethod
    def getShardDesignation(self) -> AgentShardDesignation:
        pass

    @abstractmethod
    def signalAgentEvent(self, event: AgentEvent):
        pass


class ShardContainerInterface(EntityProxyInterface):
    @abstractmethod
    def postAgentEvent(self, event: AgentEvent):
        pass

    @abstractmethod
    def getAgentShard(self, designation: AgentShardDesignation) -> AgentShardInterface:
        pass


class Shard(EntityInterface):
    def __init__(self, designation: AgentShardDesignation, name=None):
        self._running = False
        self._name = name
        self._registered_entities = dict()
        self._entity_order = []
        self._designation = designation

    @property
    def designation(self):
        return self._designation
