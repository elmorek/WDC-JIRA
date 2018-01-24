#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Jesus Rodriguez"
__license__     = "MIT"
__version__     = "0.1"
__status__      = "Prototype"

import os
from app import create_app
from flask_sript import Manager, Server, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)
manager.add_command('Shell', Shell(make_shell_context))
manager.add_command('runserver', Server(host='localhost', port=80, threaded=True))

if __name__ == '__main__':
    manager.run()
