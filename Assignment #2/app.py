from flask import Flask, request

from calcAcre import calc_acre

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def get_input():
    """
    :return:
    """
    packet = request.get_json(force=True)

    length = packet['length']

    width = packet['width']

    acre = calc_acre(length, width)

    return {"acre": acre}
    # return acre
