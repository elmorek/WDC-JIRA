#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__      = "Jesus Rodriguez"
__license__     = "MIT"
__version__     = "0.1"
__status__      = "Prototype"

from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import Required, Length


class jiraForm(Form):
    name = StringField('Name', validators=[Length(4,10), Required()])
    password = PasswordField('Password', validators=[Required()])
    JQL = TextAreaField('JQL Query', validators=[Required()])
    submit = SubmitField('Run')
