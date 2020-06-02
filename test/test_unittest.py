import unittest

from music_aekt.downloaders.zing import ZingDownloader
from music_aekt.downloaders.nhaccuatui import NCTDownloader


class TestDownloaderImplementation(unittest.TestCase):

    def setUp(self):
        pass

    def test_downloaders_init(self):
        class TestDownloader:

            def __init__(self, d, url):
                self.downloader = d
                self.song_url = url

        tests = [
            TestDownloader(ZingDownloader, 'https://mp3.zing.vn/foo'),
            TestDownloader(NCTDownloader, 'https://nhaccuatui.vn/bar')
        ]

        for test_downloader in tests:
            d = test_downloader.downloader(test_downloader.song_url)
            self.assertTrue(self, test_downloader.song_url == d.url)
            self.assertIsNotNone(self, d.path)
            self.assertIsNotNone(self, d.headers)


if __name__ == '__main__':
    unittest.main()

