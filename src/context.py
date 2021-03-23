

class Context(object):

    def __init__(self, metadata, env):
        self._metadata = metadata
        self._env = env
        self._session = None

    def env(self):
        return self._env

