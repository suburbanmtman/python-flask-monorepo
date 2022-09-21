from flask import Flask

from gvd_lib_1 import generate_name
from gvd_lib_2 import generate_id

app = Flask(__name__)


@app.route("/a/data", methods=["POST"])
def create_data():
    return {
        "name": generate_name(),
        "id": generate_id(),
    }
