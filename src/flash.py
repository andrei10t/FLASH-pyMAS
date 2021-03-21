import argparse
import logging
from agent.agent import Agent
from typing import List
from pathlib import Path
from fileutil import read_json_config, read_xml_config, find_agent

logger = logging.getLogger(__name__)


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config-json",
        required=False,
        type=lambda _p: read_json_config(Path(_p)),
        default = dict(),
        help = "Path to json config file for Loader",
    )
    parser.add_argument(
        "--config-xml",
        required=False,
        type=lambda _p: read_xml_config(Path(_p)),
        default = dict(),
        help = "Path to xml config file for Loader",
    )
    parser.add_argument(
        "--agent",
        required=False,
        type=lambda name: find_agent(name: str),
        default = Agent(),
        help = "",
    )
    return parser.parse_args(args)


