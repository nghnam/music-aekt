import os
import sys

from music_aekt import create_app


config_file = sys.argv[2] if len(sys.argv) > 1 else 'config.py'
config_file = os.path.dirname(os.path.abspath(__file__)) + '/'+ config_file
app = create_app(config_file=config_file)
