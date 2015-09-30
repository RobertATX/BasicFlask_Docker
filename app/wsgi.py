__author__ = 'Robert Donovan'

# -*- coding: utf-8 -*-

#from flask import Flask
#application = Flask(__name__)

from twoweeks import app
import twoweeks.config as config

app.run(debug=config.DEBUG, host=config.HOST)

#@application.route('/', methods=['GET'])
#def index():
#    return 'Hello world!'

#def test():
#    application.run(debug=True)

#if __name__ == '__main__':
#    test()
