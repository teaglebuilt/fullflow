

class Context(object):
    """
    Context class for project metadata
    """
    def __init__(self, metadata, env):
        self._metadata = metadata
        self._env = env
        self._session = None

    def env(self):
        return self._env
