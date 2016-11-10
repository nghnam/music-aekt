from celery import Celery

from music_aekt.downloaders.zing import ZingDownloader
from music_aekt.downloaders.nhaccuatui import NCTDownloader
from music_aekt.player import moc

app = Celery('tasks',
             backend='redis://localhost',
             broker='redis://localhost')

SAVE_LOCATION = '/tmp'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

ZING_PATTERN = 'var xml_link = "(.*?)";'

@app.task
def download(url):
    if "mp3.zing.vn" in url:
        d = ZingDownloader(url=url,
                           path=SAVE_LOCATION,
                           headers=HEADERS,
                           pattern = ZING_PATTERN)
    elif "nhaccuatui.com" in url:
        d = NCTDownloader(url=url,
                          path=SAVE_LOCATION,
                          headers=HEADERS)
    f = d.download_mp3_file()
    moc.append(f)
