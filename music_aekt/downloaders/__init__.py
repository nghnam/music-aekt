import abc


SAVE_LOCATION = '/tmp'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}


class DownloaderBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self, url, path=None, headers=None, pattern=None):
        self.url = url
        self.path = SAVE_LOCATION
        self.headers = HEADERS

    @abc.abstractmethod
    def download_mp3_file(self):
        raise NotImplementedError
