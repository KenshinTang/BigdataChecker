#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BigDataChecker

应用入口

author: Kenshin
last edited: 2018.11.30
"""

from flask import Flask, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@app.route('/', methods=['POST'])
def hello_word():
    json_data = {"code": "1112", "msg": "11111111"}
    res = jsonify(json_data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res
