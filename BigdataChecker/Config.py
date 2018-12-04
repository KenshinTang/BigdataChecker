#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BigDataChecker

接口配置

author: Kenshin
last edited: 2018.12.4
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    apiList = [
        ('n36_a_1', 'n36_a_1'),
        ('n36_a_2', 'n36_a_2'),
        ('n36_a_3', 'n36_a_3'),
        ('n36_a_5', 'n36_a_5'),
        ('n36_a_6', 'n36_a_6'),
        ('n36_a_7', 'n36_a_7'),
        ('n36_a_8', 'n36_a_8')
    ]
    user_id = StringField('user_id', validators=[DataRequired()])
    # api = SelectField('api', choices=apiList)
    submit = SubmitField('Submit')