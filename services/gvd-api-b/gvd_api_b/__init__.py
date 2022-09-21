from flask import Flask

from gvd_lib_2 import generate_id

app = Flask(__name__)


@app.route("/b/id", methods=["POST"])
def create_id():
    return {
        "id": generate_id(),
    }
