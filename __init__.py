#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Jesus Rodriguez"
__license__     = "MIT"
__version__     = "0.1"
__status__      = "Prototype"


from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(congig[config_name])

    bootstrap.init_app(app)
    with app.app_context():
        from main import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
