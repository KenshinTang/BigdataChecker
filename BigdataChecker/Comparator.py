#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
数据比较器

author: Kenshin
last edited: 2018.11.30
"""

from flask import current_app
from BigdataChecker.mode.Result import Result
import os


class Comparator(object):
    @staticmethod
    def compare(data1, data2):
        current_app.logger.debug("data1 = %s", data1)
        current_app.logger.debug("data2 = %s", data2)
        result = Result()

        if not isinstance(data1, dict) or not isinstance(data2, dict):
            result.code = Result.CODE_INNER_ERR_FORMAT
            result.msg = '系统错误, 输入数据格式有误.'
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
                result.code = Result.CODE_ERR_LACK_OF_KEY
                result.msg = '缺少字段: %s' % lackofkeys
                return result.create()
            elif len(illegalvalues) > 0:
                result.code = Result.CODE_ERR_ILLEGAL_VALUE
                for value in illegalvalues:
                    result.msg += '字段:%s 期望值:%s 实际值:%s %s' % (value[0], value[1], value[2], os.linesep)
                return result.create()

