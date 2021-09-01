from abc import ABC, abstractmethod
from entity.entity import EntityProxyInterface
from entity.configurableEntity import ConfigurableEntityInterface
from agent.agent import AgentEvent
from enum import Enum

class AgentShardDesignation(Enum):
    MESSAGING = "MESSAGING"
    IO = "IO"
	GUI = "GUI"
	MONITORING="MONITORING"
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
    def __init__(self, name=None, designation: AgentShardDesignation):
        self._running = False
        self._name = name
        self._registered_entities = dict()
        self._entity_order = []
        self._designation = designation
    
    @property
    def designation(self):
        return self._designation

    
    
    