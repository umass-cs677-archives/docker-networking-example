from flask import Flask, jsonify

ITEMS = {
    "1001": {"name": "RPCs for Dummies", "price": 14.99, "quantity": 10},
    "1002": {"name": "Xen and the Art of Surviving Graduate School", "price": 9.99, "quantity": 5}
}


app = Flask(__name__)


@app.route("/query/<item_id>")
def query(item_id):
    if item_id in ITEMS:
        return jsonify({"data": ITEMS[item_id]})
    else:
        return jsonify({"error": {"code": 404, "message": "Item not found"}})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
