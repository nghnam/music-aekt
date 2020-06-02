from celery import Celery

from music_aekt.downloaders import SongDownloader
from music_aekt.player import moc

app = Celery('tasks',
             backend='redis://localhost',
             broker='redis://localhost')


@app.task
def download(url):
    d = SongDownloader(url)
    moc.append(d.download())
