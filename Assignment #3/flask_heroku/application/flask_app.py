# import modules
from flask import Flask, request, jsonify

from calcAcre import calc_acre

app = Flask('__name__')


@app.route('/', methods=['GET', 'POST'])
def get_input():
    packet = request.get_json()

    length = packet['length']

    width = packet['width']

    area_acres = calc_acre(length, width)

    return jsonify(packet, area_acres)
