"""Console script for flash_pymas."""
import argparse
import sys


def main():
    # """Console script for flash_pymas."""
    # parser = argparse.ArgumentParser()
    # parser.add_argument('_', nargs='*')
    # args = parser.parse_args()

    # print("Arguments: " + str(args._))
    # print("Replace this message by putting your code into "
    #       "flash_pymas.cli.main")
    # return 0
    params = parse_args(sys.argv[1:])


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="flash",
        usage="%(prog)s -pylon -agent A -shard message -agent B -shard knowledge",
        description="Deploy agents",
    )
    parser.add_argument(
        "-agent",
        required=True,
        metavar="AGENT",
        help="agent to be deployed, specify name, can be used with -shard type",
    )
    parser.add_argument(
        "-shard",
        choices=["message", "monitor", "gui", "control", "knowledge"],
        required=True,
        metavar="SHARD",
        help="shard type, pick a choice",
    )
    parser.add_argument(
        "-pylon",
        required=True,
        metavar="SERVICE",
        help="for now just give a port, all of them are websockets",
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
