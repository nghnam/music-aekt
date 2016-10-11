import os.path
import subprocess 

from flask import current_app


def mocp(*args):
    command = ['mocp'] + list(args)
    output = ''
    exit_code = 0
    try:
        output = subprocess.check_output(command, shell=False, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        exit_code = e.returncode
    return output, exit_code

def play():
    return mocp("-p")

def stop():
    return mocp("-s")

def pause():
    return mocp("-P")

def unpause():
    return mocp("-U")

def next_():
    return mocp("-f")

def prev():
    return mocp("-r")

def clear():
    return mocp("-c")

def append(mp3_file):
    if os.path.isfile(mp3_file):
        return mocp("-a", mp3_file)

def show_current_song():
    return mocp("-i")

def show_play_list():
    playlist_file = current_app.config.get('MOC_PLAYLIST')
    playlist = []

    if not os.path.isfile(playlist_file):
        return playlist

    with open(playlist_file) as f:
        for line in f:
            if line.startswith('#EXTINF'):
                length, title = line.split('#EXTINF:')[1].split(',', 1)
                playlist.append((length, title.strip()))

    return playlist
