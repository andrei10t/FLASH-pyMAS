from abc import ABC, abstractmethod
from entity.entityProxy import EntityProxyInterface
from entity.configurableEntity import ConfigurableEntityInterface
from agent import AgentEvent

class AgentShardDesignation:
    ...


class AgentShardInterface(ConfigurableEntityInterface):
    @abstractmethod
    def getShardDesignation(self) -> AgentShardDesignation:
        pass

    @abstractmethod
    def signalAgentEvent(self, event: AgentEvent):
        pass


class ShardContainer(EntityProxyInterface):
    @abstractmethod
    def postAgentEvent(self, event: AgentEvent):
        pass

    @abstractmethod
    def getAgentShard(self, designation: AgentShardDesignation) -> AgentShardInterface:
        pass