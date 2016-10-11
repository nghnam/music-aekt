from flask import Flask

from music_aekt.controllers.main import main

def create_app(config_file):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app.register_blueprint(main)
    
    return app
