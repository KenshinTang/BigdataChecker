#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
比较结果

author: Kenshin
last edited: 2018.11.30
"""

from flask import jsonify, current_app


class Result(object):
    CODE_INNER_ERR_FORMAT = -1
    CODE_SUCCESS = 0
    CODE_ERR_LACK_OF_KEY = 1
    CODE_ERR_ILLEGAL_VALUE = 2

    code = CODE_SUCCESS
    msg = ''
    __data = {}

    def __init__(self, code=0, msg=''):
        self.code = code
        self.msg = msg
        self.__data = {'code': self.code, 'msg': self.msg}
        super().__init__()

    def create(self):
        self.__data['code'] = self.code
        self.__data['msg'] = self.msg
        current_app.logger.debug('compare result = %s', self.__data)
        current_app.logger.debug('')
        r = jsonify(self.__data)
        r.headers['Access-Control-Allow-Origin'] = '*'
        return r
