"""
export INFISICAL_API_URL="***"
export INFISICAL_TOKEN="***"

then run:
python sdk/flask_hello_world.py
"""
import os
import time

from flask import Flask
from infisical import InfisicalClient

app = Flask(__name__)

INFISICAL_API_URL = os.environ.get("INFISICAL_API_URL")
INFISICAL_TOKEN = os.environ.get("INFISICAL_TOKEN")

client = InfisicalClient(site_url=INFISICAL_API_URL, token=INFISICAL_TOKEN)


@app.route("/")
def hello_world():
    start = time.time()
    name = client.get_secret(secret_name="NAME", environment="dev", type="shared")
    return f"Hello! My name is: {name.secret_value}, time: {round(time.time() - start, 2)}"


if __name__ == "__main__":
    app.run(debug=True)
