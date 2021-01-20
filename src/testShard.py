from unittest import TestCase
# from unittest.mock import patch
from shard import ShardContainerInterface
from agent.agent import Agent

class ShardContainer(ShardContainerInterface):
    def postAgentEvent(self, event: AgentEvent):
        if isinstance(event, AgentWave):
        pass

class TestShard(TestCase):
    proxy = ShardContainer()