# import modules
from flask import Flask, request, jsonify

from area import area_in_acres


def get_input():
    meg = "This is just a small test"
    return meg


# instantiate a flask object
app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def get_input():
    # A Flask app to take inputs for area
    # module function and returns acres
    packet = request.get_json()
    length = packet['length']
    width = packet['width']
    area_acres = area_in_acres(length, width)
    # return jsonify(area_acres)
    return jsonify('length (feet):{}'.format(packet['length']),
                   'width (feet):{}'.format(packet['width']),
                   'area (acres):{}'.format(area_acres))
