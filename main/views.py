#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Jesus Rodriguez"
__license__     = "MIT"
__version__     = "0.1"
__status__      = "Prototype"

from flask import render_template
from . import main

@main.route('/', methods=['GET'])
def index():

    return render_template('index.html')
