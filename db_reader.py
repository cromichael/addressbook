

class DBReader():

    _index = {}

    def __init__(self, config):
        self.config = config
        self._connect()

    def _connect(self):
        print('Connecting to database ...')

    def search(self, query):
        print('searching database for', query)
