__author__ = 'Robert Donovan'

from twoweeks import app
import twoweeks.config as config

if __name__ == "__main__":
    app.run(debug=config.DEBUG, host=config.HOST)
    # @application.route('/', methods=['GET'])