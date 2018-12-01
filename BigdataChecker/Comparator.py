#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
数据比较器

author: Kenshin
last edited: 2018.11.30
"""

from flask import jsonify, current_app
import os


class Comparator(object):
    def compare(self, data1, data2):
        current_app.logger.debug("data1 = %s", data1)
        current_app.logger.debug("data2 = %s", data2)
        result = self.Result()

        if not isinstance(data1, dict) or not isinstance(data2, dict):
            result.code = -1
            result.msg = '格式错误'
            return result.create()
        else:
            lackofkeys = []
            illegalvalues = []
            for k, v in data2.items():
                if k not in data1:
                    lackofkeys.append(k)
                elif data1[k] == v:
                    continue
                else:
                    illegalvalues.append([k, v, data1[k]])

            if len(lackofkeys) > 0:
                result.code = 1
                result.msg = '缺少字段: %s' % lackofkeys
                return result.create()
            elif len(illegalvalues) > 0:
                result.code = 2
                for value in illegalvalues:
                    result.msg += '字段:%s 期望值:%s 实际值:%s %s' % (value[0], value[1], value[2], os.linesep)
                return result.create()

    class Result(object):
        code = 0
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
