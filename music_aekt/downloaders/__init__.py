from .zing import ZingDownloader
from .nhaccuatui import NCTDownloader


class SongDownloader(object):

    def __init__(self, url):
        self.downloader = self._get_downloader(url)

    def _get_downloader(self, url):
        if "mp3.zing.vn" in url:
            d = ZingDownloader
        elif "nhaccuatui.com" in url:
            d = NCTDownloader
        else:
            raise Exception('No downloader found')

        return d(url)

    def download(self):
        return self.downloader.download_mp3_file()
