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
from BigdataChecker.utils.SystemUtils import AndroidSystemUtils


class ConfigForm(FlaskForm):
    apiList = [
        ('n603_a_1', 'n603_a_1'),
        ('n603_a_2', 'n603_a_2'),
        ('n603_a_3', 'n603_a_3'),
        ('n603_a_5', 'n603_a_5'),
        ('n603_a_6', 'n603_a_6'),
        ('n603_a_7', 'n603_a_7'),
        ('n603_a_8', 'n603_a_8')
    ]
    clientList = [
        ('stb', 'stb'),
        ('phone', 'phone'),
        ('pad', 'pad'),
        ('pc', 'pc')
    ]
    networkList = [
        ('cable', 'cable'),
        ('wifi', 'wifi'),
        ('4g', '4g'),
        ('3g', '3g'),
        ('2g', '2g')
    ]
    systemList = [
        ('ios', 'ios'),
        ('Android', 'Android'),
        ('PC', 'PC'),
        ('Linux', 'Linux')
    ]
    api = SelectField('api', choices=apiList)
    user_id = StringField('user_id', validators=[DataRequired()])
    device_id = StringField('device_id', validators=[DataRequired()])
    mac = StringField('mac', validators=[DataRequired()], default=AndroidSystemUtils.getMac())
    client_type = SelectField('client_type', choices=clientList)
    network_type = SelectField('network_type', choices=networkList)
    apk_version = StringField('apk_version', validators=[DataRequired()])
    system_name = SelectField('system_name', choices=systemList)
    system_version = StringField('system_version', validators=[DataRequired()], default=AndroidSystemUtils.getSystemVersion())
    region_code = StringField('region_code')
    server_time = StringField('server_time', validators=[DataRequired()])
    sp_id = StringField('sp_id', validators=[DataRequired()])
    platform_id = StringField('platform_id', validators=[DataRequired()])

    submit = SubmitField('Submit')
