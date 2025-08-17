"""Web service that accepts a text and returns its language code."""

from flask import Flask
from flask import request, jsonify
import langdetect as ld
import os  # Import the os module

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Returns a description of the web service."""
    return "Hello!! This is an app to detect the language of a document"

@app.route("/detect", methods=['GET'])
def detect():
    """Identifies the language of the text."""
    query = request.args.get('text')
    language = ld.detect(query)
    return language

@app.route("/instance", methods=['GET'])
def instance():
    """Returns the first directory in '/var/lib/cloud/instances/'."""
    try:
        dirs = os.listdir('/var/lib/cloud/instances/')
        if dirs:
            return jsonify({"first_instance": dirs[0]})
        else:
            return jsonify({"error": "No directories found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
