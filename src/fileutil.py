from pathlib import Path
import os
import json
# class FileUtil(object):
#     settings = None
#
#     def __init__(self):
#         self.settings = Settings()

# convert json at path in dict
def read_json_config(path: Path):
    ...


# convert xml at path in dict
def read_xml_config(path: Path):
    ...

# python3 flash --agent 1234 --agent 2345 --agent 3456
# find by name the predefined agent in configs/agents
def get_agent(name):
    path = "/Users/atoader/projects/pyMas/configs/agents"
    elem=os.listdir(path)
    print(elem)
    if os.path.isfile(path):
    #    json load
    else:
        print("")
        raise SystemExit(12)


# find by name the predefined agent in configs/shards
def get_shard(name):
    ...

# python3 flash --agents 1234 2345 3456 4567
# find by name the predefined agent in configs/agents
def get_agents(name):
    ...


# find by name the predefined agent in configs/shards
def get_shards(name):
    ...

def get_full_filename(filename):
    full_filename = os.path.join()

    # check folder exists
    # create folder if doesn't exist
    if not os.path.exists():
        try:
            os.makedirs()
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return full_filename