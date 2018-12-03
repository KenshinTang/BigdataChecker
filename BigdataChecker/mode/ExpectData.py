#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
预期结果构建, 数据结构如下(字段可嵌套):
{接口名: {字段key: [字段value, 是否不可为空, 是否包含子字段]}}
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
        cls.__data['n603_a_1'] = {'user_id': ['', 1, 0],
                                  'device_id': ['', 1, 0],
                                  'mac': ['', 1, 0],
                                  'client_type': ['', 1, 0],
                                  'network_type': ['', 1, 0],
                                  'apk_version': ['', 1, 0],
                                  'system_name': ['', 1, 0],
                                  'system_version': ['', 1, 0],
                                  'region_code': ['', 0, 0],
                                  'server_time': ['', 1, 0],
                                  'page_sid': ['', 1, 0],
                                  'play_sid': ['', 2, 0],
                                  'page_id': ['', 1, 0],
                                  'asset_id': ['', 2, 0],
                                  'category_id': ['', 2, 0],
                                  'video_id': ['', 2, 0],
                                  'video_name': ['', 2, 0],
                                  'video_type': ['', 2, 0],
                                  'episode_id': ['', 2, 0],
                                  'media_id': ['', 2, 0],
                                  'playbill_start_time': ['', 2, 0],
                                  'playbill_length': ['', 2, 0],
                                  'playbill_name': ['', 2, 0],
                                  'sp_id': ['', 1, 0],
                                  'heartbeat_type': ['', 1, 0],
                                  'latitude': ['', 2, 0],
                                  'longitude': ['', 2, 0],
                                  'platform_id': ['', 1, 0]
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
        cls.setContent(result, 'user_id', 'value')
        cls.setContent(result, 'device_id', 'value')
        return result

    @classmethod
    def setContent(cls, content, key, value):
        if content[key][2] == 0:
            content[key][0] = value
        else:
            # todo: support dict here.
            print('support dict here')
        return content
