from celery import Celery

from music_aekt.downloaders.zing import ZingDownloader
from music_aekt.player import moc

app = Celery('tasks',
             backend='redis://localhost',
             broker='redis://localhost')

SAVE_LOCATION = '/tmp'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

PATTERN = 'var xml_link = "(.*?)";'

@app.task
def download(url):
    z = ZingDownloader(url=url, path=SAVE_LOCATION, headers=HEADERS, pattern = PATTERN)
    f = z.download_mp3_file()
    moc.append(f)
