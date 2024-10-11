from flask import Flask
from flask import render_template
from flask.json import jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/api")
def api_verification():
    return jsonify({"version": 1.0})