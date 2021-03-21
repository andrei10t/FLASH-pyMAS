from typing import Mapping

class Loader:
    _config = None

    def __init__(self, components_config: Mapping):
        self._config = components_config
