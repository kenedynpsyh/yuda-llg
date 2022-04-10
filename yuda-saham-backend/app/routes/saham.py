import requests
from flask import Blueprint, jsonify, request

routes_saham = Blueprint("saham", __name__)

@routes_saham.route("/",methods=["post"])
def lists_saham():
    add_url = request.get_json()
    results = requests.get("http://akian.id/%s.txt" % add_url['data'])
    print(results.text)
    return jsonify(message=results.text)