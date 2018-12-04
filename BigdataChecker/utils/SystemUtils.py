#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
SystemUtils

获取系统属性

author: Kenshin
last edited: 2018.11.30
"""

import os, re

class AndroidSystemUtils(object):
    @staticmethod
    def getMac():
        # content = os.popen('adb shell cat /sys/class/net/eth0/address').read().strip()
        # matchObj = re.search(r'[0-9a-fA-F]{2}([:-][0-9a-fA-F]{2}){5}', content)
        # return matchObj.group()
        return os.popen('adb shell cat /sys/class/net/eth0/address').read().strip()

    @staticmethod
    def getSystemVersion():
        return os.popen('adb shell getprop ro.build.version.release').read().strip()

class IOSSystemUtils(object):
    @staticmethod
    def getMac():
        return ''

    @staticmethod
    def getSystemVersion():
        return ''

class LinuxSystemUtils(object):
    @staticmethod
    def getMac():
        return ''

    @staticmethod
    def getSystemVersion():
        return ''
