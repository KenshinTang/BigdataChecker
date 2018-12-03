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

    def init(self):
        self.__data['n603_a_1'] = {'user_id': ['', 1, 0],
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
                                   'platform_id': ['', 1, 0],
                                   }

        self.__data['n603_a_6'] = {"event_name": "open_page", "event_source": "p_index_vod",
                                   "event_target": "p_index_channel", "event_time": "1543595417180",
                                   "event_value": {"video_name": "", "page_type": "p_index_channel",
                                                   "special_id": "",
                                                   "auth_state": "", "asset_id": "",
                                                   "special_name": "",
                                                   "product_name": "", "episode_id": "",
                                                   "category_id": "",
                                                   "product_id": "", "media_id": "",
                                                   "recommend_code": "",
                                                   "video_id": ""},
                                   "page_sid": "3997538a1f40469c99a90c79f5a9d6f8",
                                   "session_id": "9362dc6bb8634c83b9a9bdd6e9fda114",
                                   "apk_version": "1.1.0.0.2.SC-HuaCaiTV-APHONE.0.0_Release",
                                   "client_type": "phone",
                                   "counter": 36824643, "create_time": 1543595417180,
                                   "device_id": "a4:08:ea:5b:49:1b",
                                   "log_type": "behavior", "mac": "a4:08:ea:5b:49:1b",
                                   "network_type": "wifi",
                                   "platform_id": "xjcbc", "region_code": "",
                                   "sdk_version": "v2.16.4",
                                   "sp_id": "hctv_mobile", "system_name": "Android",
                                   "system_version": "samsung/hero2qltezc/hero2qltechn:8.0.0/R16NW/G9350ZCS3CRJ2:user/release-keys",
                                   "user_id": "gt_a4:08:ea:5b:49:1b"}
                                   # , "test_Redundant_value": "1"}

    def build(self, apiName):
        if apiName == 'n603_a_1':
            result = {}
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
        return result

    def getExpectData(self, apiName):
        return self.__data[apiName]
