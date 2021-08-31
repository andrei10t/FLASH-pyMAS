from abc import ABC, abstractmethod
from entity.entity import EntityProxyInterface
from entity.configurableEntity import ConfigurableEntityInterface
from agent.agent import AgentEvent


class AgentShardDesignation:
    ...


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
