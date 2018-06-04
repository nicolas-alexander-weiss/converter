#!flask/bin/python
from flask import Flask, abort, jsonify, make_response, request
from flask import url_for

app = Flask(__name__)

@app.route("/convert/<string:input_quantity>/<string:output_type>", methods=["GET"])
def convert(input_quantity, output_type):
    return "Not yet working.\n\nYou wanted to convert " + input_quantity + " into " + output_type


if __name__ == "__main__":
    app.run(debug=True)