import re
from xml.etree import ElementTree as ET

import requests


class NCTDownloader(object):

    def __init__(self, url, path, headers=None, pattern=None):
        self.url = url
        self.headers = headers
        self._rule = "http://www.nhaccuatui.com/bai-hat"
        self._pattern = pattern if pattern \
                                else 'player.peConfig.xmlURL = "(.*?)";'
        self.path = path
        self.filename = ''
        self.metadata = None
        self.download_url = ''
        self._get_metadata()
        self._extract_mp3_link()
        self._create_file_name()

    def _check_url(self):
        return True if self._rule in self.url else False

    def _get_page_source(self):
        if self._check_url():
            r = requests.get(url=self.url, headers=self.headers)
            return str(r.content)
        else:
            return ''

    def _extract_metadata_url(self):
        html = self._get_page_source()
        metadata_url = re.findall(self._pattern, html)
        return metadata_url[0] if metadata_url else ''

    def _get_metadata(self):
        metadata_url = self._extract_metadata_url()
        if metadata_url:
            r = requests.get(url=metadata_url, headers=self.headers)
            self.metadata = str(r.content)

    def _get_cover(self):
        # http://image.mp3.zdn.vn/cover3_artist/3/3/33a0b0292c3fac8cc63a529fccbb1df9_1470739610.jpg
        pass

    def _extract_mp3_link(self):
        if self.metadata:
            tree = ET.fromstring(self.metadata)
            for url in tree.findall('./track/location'):
                self.download_url = url.text.strip()

    def _create_file_name(self):
        if self.download_url:
            self.filename = self.download_url.split('/')[-1]
            
    def download_mp3_file(self):
        if self.download_url:
            location = self.path + '/' + self.filename
            r = requests.get(self.download_url,
                             headers=self.headers,
                             stream=True)
            with open(location, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            r.close()
            return location
        return ''
