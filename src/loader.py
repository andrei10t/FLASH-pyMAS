from typing import Mapping
from settings import Settings

class Loader:
    _config = None
    _settings = None

    def __init__(self, components_config: Mapping):
        self._config = components_config
        self._settings = Settings()