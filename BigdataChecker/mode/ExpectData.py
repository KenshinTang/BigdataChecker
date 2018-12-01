#!/usr/bin/python
# -*- coding: utf-8 -*-


class ExpectDataBuilder(object):
    __data = {}

    def __init__(self):
        super().__init__()
        self._init()

    def _init(self):
        self.__data['n603_a_1'] = {'event_name': 'open_page', 'event_source': 'p_index_vod'}
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

    def getExpectData(self, api):
        return self.__data[api]
