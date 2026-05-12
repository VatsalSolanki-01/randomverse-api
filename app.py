from flask import Flask, jsonify, render_template
import json
import random
import os

app = Flask(__name__)

DATA_FILE = "quotes.json"


def load_data():
    """
    Load JSON data from local file.
    """

    try:

        if not os.path.exists(DATA_FILE):
            raise FileNotFoundError(f"{DATA_FILE} not found")

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return data

    except json.JSONDecodeError:
        return None

    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def get_random_item(category):
    """
    Return a random item from a category.
    """

    data = load_data()

    if not data:
        return {
            "error": "Unable to load data"
        }, 500

    if category not in data:
        return {
            "error": f"Category '{category}' not found"
        }, 404

    items = data.get(category, [])

    if not items:
        return {
            "error": f"No data available for '{category}'"
        }, 404

    return {
        "category": category[:-1],
        "message": random.choice(items)
    }, 200


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api_info():

    return jsonify({
        "application": "RandomVerse API",
        "status": "running",
        "available_endpoints": [
            "/",
            "/health",
            "/quote",
            "/advice",
            "/joke"
        ]
    })


@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })


@app.route("/quote")
def quote():

    response, status_code = get_random_item("quotes")

    return jsonify(response), status_code


@app.route("/advice")
def advice():

    response, status_code = get_random_item("advice")

    return jsonify(response), status_code


@app.route("/joke")
def joke():

    response, status_code = get_random_item("jokes")

    return jsonify(response), status_code


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )