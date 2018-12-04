#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BigDataChecker

应用入口

author: Kenshin
last edited: 2018.11.30
"""

from flask import Flask, jsonify, request, render_template
from BigdataChecker.mode.ExpectData import ExpectDataBuilder
from BigdataChecker.Comparator import Comparator
from BigdataChecker.Config import ConfigForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'big-data-checker'


@app.route('/', methods=['GET', 'POST'])
def main():
    inputData = json.loads(request.data)
    apiName = inputData['get_source']
    expectData = ExpectDataBuilder.build(apiName)

    app.logger.debug('start comparing %s', apiName)
    result = Comparator.compare(inputData['get_data'], expectData)
    return result

@app.route('/config')
def getConfig():
    form = ConfigForm()
    return render_template('config.html', form=form)


def buildExpectedResult():
    pass


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    ExpectDataBuilder.init()
    app.run(debug=True)


