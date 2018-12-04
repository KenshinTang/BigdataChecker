#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BigDataChecker

接口配置

author: Kenshin
last edited: 2018.12.4
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired()])
    submit = SubmitField('Submit')