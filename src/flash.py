import argparse
import logging
import sys
from agent.agent import Agent
from shard import AgentShardDesignation
from typing import List
from pathlib import Path
from fileutil import read_json_config, read_xml_config, get_agent, get_shard
from loader import Loader

logger = logging.getLogger(__name__)


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config-json",
        required=False,
        # nu e musai calea, se poate si simplu config.json cat timp e mereu in configs/
        type=lambda _p: read_json_config(Path(_p)),
        default=dict(),
        help="Path to json config file for package",
    )
    parser.add_argument(
        "--config-xml",
        required=False,
        type=lambda _p: read_xml_config(Path(_p)),
        default=dict(),
        help="Path to xml config file for package",
    )
    parser.add_argument(
        "--agent",
        required=False,
        type=lambda name: get_agent(name),
        default=Agent(),
        action="append",
        help="Deploy predefined agent specifying its name",
    )
    parser.add_argument(
        "--agents",
        required=False,
        type=lambda name: get_agent(name),
        default=Agent(),
        nargs="+",
        # type = Agent,
        help="Deploy predefined agent specifying its name",
    )
    parser.add_argument(
        "--shards",
        required=False,
        type=lambda name: get_shard(name),
        default=AgentShardDesignation(),
        nargs="+",
        help="Deploy predefined shard specifying its name",
    )
    return parser.parse_args(args)


def main():
    params = parse_args(sys.argv[1:])
