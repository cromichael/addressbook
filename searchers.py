from csv_reader import CSVReader
from db_reader import DBReader

class SearcherFactory:

    def __init__(self):
        self._searchers = {}

    def register(self, searcher_type, searcher):
        self._searchers[searcher_type] = searcher

    def get_searcher(self, config):
        searcher = self._searchers.get(config['searcher'])
        if not searcher:
            raise ValueError(config['searcher'])
        return searcher(config)


factory = SearcherFactory()
# Register searchers
factory.register('csvfsreader', CSVReader)
factory.register('dbreader', DBReader)