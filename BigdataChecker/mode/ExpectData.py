#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
预期结果构建, 数据结构如下(字段可嵌套):
{接口名: {字段key: [字段value, 是否不可为空, 检查等级-0不检查-1弱检查-2强检查]}}
是否不可为空 : 0可为空, 1不可为空, 2条件为空
检查等级    : 0不检查, 1弱检查(只检查非空,格式等), 2强检查(检查值是否正确)
eg:
{'n603_a_1': {'event_name': ['open_page', 1, 0] ,
              'system_name': ['', 0, 0]}
 'n603_a_6': {'event_name': ['open_page', 1, 0] ,
              'event_value': [{'asset_id': ('movie', 1, 0],
                               'category_id': ['看点', 1, 0]}, 1, 1]}
}

author: Kenshin
last edited: 2018.11.30
"""

from flask import current_app
from BigdataChecker.utils.SystemUtils import AndroidSystemUtils


class ExpectDataBuilder(object):
    __data = {'n603_a_1': {},  # 终端心跳上报
              'n603_a_2': {},  # 播放行为上报
              'n603_a_3': {},  # 错误上报
              'n603_a_5': {},  # 终端开机上报
              'n603_a_6': {},  # 用户行为上报
              'n603_a_7': {},  # 性能日志上报
              'n603_a_8': {}}  # 应用会话信息上报

    @classmethod
    def init(cls):
        cls.__data['n603_a_1'] = {'user_id': ['', 1, 2],
                                  'device_id': ['', 1, 1],
                                  'mac': ['', 1, 2],
                                  'client_type': ['', 1, 1],
                                  'network_type': ['', 1, 1],
                                  'apk_version': ['', 1, 1],
                                  'system_name': ['', 1, 1],
                                  'system_version': ['', 1, 1],
                                  'region_code': ['', 0, 2],
                                  'server_time': ['', 1, 1],
                                  'page_sid': ['', 1, 2],
                                  'play_sid': ['', 2, 2],
                                  'page_id': ['', 1, 2],
                                  'asset_id': ['', 2, 2],
                                  'category_id': ['', 2, 2],
                                  'video_id': ['', 2, 2],
                                  'video_name': ['', 2, 2],
                                  'video_type': ['', 2, 2],
                                  'episode_id': ['', 2, 2],
                                  'media_id': ['', 2, 2],
                                  'playbill_start_time': ['', 2, 2],
                                  'playbill_length': ['', 2, 2],
                                  'playbill_name': ['', 2, 2],
                                  'sp_id': ['', 1, 2],
                                  'heartbeat_type': ['', 1, 2],
                                  'latitude': ['', 2, 1],
                                  'longitude': ['', 2, 1],
                                  'platform_id': ['', 1, 1]
                                  }

    @classmethod
    def build(cls, apiName):
        if apiName == 'n603_a_1':
            result = cls.buildN603a1()
        elif apiName == 'n603_a_2':
            result = {}
        elif apiName == 'n603_a_3':
            result = {}
        elif apiName == 'n603_a_5':
            result = {}
        elif apiName == 'n603_a_6':
            result = {}
        elif apiName == 'n603_a_7':
            result = {}
        elif apiName == 'n603_a_8':
            result = {}
        else:
            result = {}
            current_app.logger.error('%s is not supported.' % apiName)

        current_app.logger.debug('expect data of %s is: %s' % (apiName, result))
        return result

    @classmethod
    def buildN603a1(cls):
        result = cls.__data['n603_a_1']
        cls.__setContent(result, 'mac', AndroidSystemUtils.getMac())
        cls.__setContent(result, 'system_version', AndroidSystemUtils.getSystemVersion())
        return result

    @classmethod
    def __setContent(cls, content, key, value):
        content[key][0] = value
        return content

