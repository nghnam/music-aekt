import os 
SAVE_LOCATION = '/tmp'

HOME_DIRECTORY = os.environ['HOME']
MOC_DIRECTORY = HOME_DIRECTORY + '/.moc'
MOC_PLAYLIST = MOC_DIRECTORY + '/playlist.m3u'

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

USERS = {'username here': 'password here'}

SECRET_KEY = 'secret key here'
