from unittest import TestCase

# from unittest.mock import patch
from shard import ShardContainer
from agent.agent import Agent


class TestAgent(TestCase):
    agent = Agent()
    print(agent.funct())
