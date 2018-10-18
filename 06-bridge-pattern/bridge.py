import abc
import urllib.request

class ResourceContent:

    def __init__(self, impl):
        self.impl = impl

    def show_content(self, path):
        self.impl.fetch(path)


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes that fetch content
    """

    @abc.abstractmethod
    def fetch(self, path):
        pass


class URLFetcher(ResourceContentFetcher):
    """
    Implement the interface
    """

    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)


class LocalFileFetcher(ResourceContentFetcher):
    """
    Implement the interface
    """

    def fetch(self, path):
        with open(path) as f:
            print(f.read())


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')
    print('=' * 20)
    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('bridge.py')


if __name__ == '__main__':
    main()
