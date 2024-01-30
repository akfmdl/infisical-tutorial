"""
export INFISICAL_API_URL="***"
export INFISICAL_TOKEN="***"

then run:
infisical run --env dev -- python sdk/flask_hello_world.py
"""
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME")
    return f"Hello! My name is: {name.secret_value}"


if __name__ == "__main__":
    app.run(debug=True)
