import csv
import string
import re

class CSVReader():

    _index = {}

    def __init__(self, config):
        self.config = config
        self._header = None
        self._readFile()

    def _build_n_gram(self, key):
        ngrams = []
        # strip out non-alphanums
        key=re.sub(r'[^a-zA-Z0-9]+', '', key).lower()
        for i in range(len(key)+1):
            for j in range(i+1, len(key)+1):
              ngrams.append(key[i:j])
        
        # print(ngrams)
        return ngrams

    # Read in csv file and build a dictionary index of the corpus
    def _readFile(self):

        with open(self.config['csvfile']) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')                                
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self._header = ",".join(row)
                    line_count += 1
                else:
                    for key in row:                        
                        # build an n-gram from key                        
                        for k in self._build_n_gram(key):
                            if k not in self._index:
                                self._index[k] = []
                            self._index[k].append(row)

                    line_count += 1

    def search(self, query):
        # add header
        # normalize result with a set
        search_result = {self._header}
        try:
            for addr in self._index[query.lower()]:
                search_result.add(",".join(addr))
        except KeyError:
            print('Cannot find', query)
            return []

        return "\n".join(search_result)
