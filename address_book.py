import argparse
import yaml
import searchers

def main():

    parser = argparse.ArgumentParser(description='Address Book')
    parser.add_argument('-cf','--configYaml', help='Configuration Yaml', required=True)
    parser.add_argument('-qs','--queryString', help='Configuration Yaml', required=True)

    args = vars(parser.parse_args())

    ab = AddressBook(args)
    print(ab.search(args['queryString']))

class AddressBook:

    def __init__(self, config):

        with open(config['configYaml'], 'r') as stream:
            try:
                yml = yaml.load(stream, Loader=yaml.SafeLoader)
                if not yml[0]['config']:
                    print ('No config stanza in yaml')
                    sys.exit(1)
                else:
                    self.config = yml.pop(0)['config']
                    self.tests = yml
            except yaml.YAMLError as err:
                print(err)
                sys.exit(1)

        self.__initSearcher()


    def __initSearcher(self):
        # Get searcher object from searcher factory
        # Inject the config object to searcher
        self.searcher = searchers.factory.get_searcher(self.config)

    def search(self, query):
        return self.searcher.search(query)        

if __name__ == '__main__':
    main()
