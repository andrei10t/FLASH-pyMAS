from pathlib import Path

# class FileUtil(object):
#     settings = None
#
#     def __init__(self):
#         self.settings = Settings()

# convert json at path in dict
def read_json_config(path: Path):
    ...

#convert xml at path in dict
def read_xml_config(path: Path):
    ...

#find by name the predefined agent in configs/agents
def get_agent(name):
    ...

#find by name the predefined agent in configs/shards
def get_shard(name):
    ...
