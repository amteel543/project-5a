"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

from mypymongo import brevet_insert, brevet_fetch

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############

@app.route("/_fetch")

def fetch():

    try: 

        time, distance, control_list = brevet_fetch()

        return flask.jsonify(result = {"time": time, "distance": distance, "control_list": control_list}, status=1, message="Successfully fetched!")

    except:

        return flask.jsonify(result={}, status=0, message="Something went wrong!")

@app.route("/_insert", methods=["POST"])

def insert():

    try:

        input_json = request.json

        time = input_json["time"]

        distance = input_json["distance"]

        control_list = input_json["control_list"] 

        insertion = brevet_insert(time, distance, control_list)

        return flask.jsonify(result={}, message="Inserted!", status=1, mongo_id=insertion)

    except:
        
        return flask.jsonify(result={}, message="Something went wrong!", status=0, mongo_id='None')

@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")

    km = request.args.get('km', 999, type=float)
    br_dis = request.args.get('br_dis', 999, type=float)
    start_time = request.args.get('start_time', type=str)
    start_time = arrow.get(start_time, 'YYYY-MM-DDTHH:mm')

    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))

    open_time = acp_times.open_time(km, br_dis, start_time).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, br_dis, start_time).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
