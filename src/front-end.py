from flask import Flask, jsonify
import os
import requests

catalog_address = os.environ["CATALOG_ADDRESS"]

app = Flask(__name__)


@app.route("/lookup/<item_id>")
def lookup(item_id):
    response = requests.get("http://{catalog_address}/query/{item_id}".format(
        catalog_address=catalog_address, item_id=item_id))
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": {"code": 505, "message": "Iternal server error"}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
