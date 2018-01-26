#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Jesus Rodriguez"
__license__     = "MIT"
__version__     = "0.1"
__status__      = "Prototype"

from flask import render_template, redirect, url_for
from flask import current_app as app
from . import main
from .forms import Jira
from jira import JIRA

@main.route('/', methods=['GET', 'POST'])
def index():
    jiraForm =Jira()
    jiraForm.instance.choices = [(value , key) for key, value in app.config['JIRA_INSTANCES'].items()]
    return render_template('index.html', jiraForm=jiraForm)

    if jiraForm.validate_on_submit():
        options = {
            'server' : jiraForm.instance.data,
            'verify' : False,
            'validate' : True
        }
        if str(jiraForm.instance.data).startswith('https'):
            connection = JIRA(
                options = options,
                basic_auth = (jiraForm.user.data, jiraForm.password.data)
            )
        else:
            connection = JIRA(
                options = options,
            )

        return redirect(url_for('index2', projectsLoaded=True))

@main.route('/index2', methods=['GET'])
def index2(projects):
    jiraForm =Jira()
    projects = [(project.name, project.id) for project in connection.projects()]
    jiraForm.projects.choices = projects
    return render_template('index.html', jiraForm=jiraForm, projectsLoaded=True)
