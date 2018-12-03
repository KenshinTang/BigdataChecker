#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BigDataChecker

应用入口

author: Kenshin
last edited: 2018.11.30
"""

from flask import Flask, jsonify, request
from BigdataChecker.mode.ExpectData import ExpectDataBuilder
from BigdataChecker.Comparator import Comparator
import json

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def hello_word():
    json_data = {"code": "1112", "msg": "11111111"}
    res = jsonify(json_data)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


@app.route('/', methods=['GET', 'POST'])
def main():
    inputData = json.loads(request.data)
    apiName = inputData['get_source']
    expectData = ExpectDataBuilder.build(apiName)

    app.logger.debug('start comparing %s', apiName)
    result = Comparator.compare(inputData['get_data'], expectData)
    return result


def buildExpectedResult():
    pass


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    ExpectDataBuilder.init()
    app.run(debug=True)


