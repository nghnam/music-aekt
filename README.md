music-aekt
==========

Relax music player

Require
=======

1, Music on console
https://moc.daper.net/

Debian/Ubuntu
```
sudo apt-get install moc
```

Other:
https://moc.daper.net/node/89

2, Flask/Celery/Python 3.x

3, Redis (broker)

Support source
==============
Now only support music in mp3.zing.vn

Config
======
config.py


Run
===
1, Music on console
$ mocp -S

2, Redis
# service redis-server start

2, Celery
$ celery worker -A music_aekt.tasks --loglevel=info

3, Flask
$ python app.py
