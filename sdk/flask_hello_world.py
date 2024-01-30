"""
export INFISICAL_API_URL="***"
export INFISICAL_TOKEN="***"

then run:
python sdk/flask_hello_world.py
"""
import os
from flask import Flask
from infisical import InfisicalClient

app = Flask(__name__)

INFISICAL_API_URL = os.environ.get("INFISICAL_API_URL")
INFISICAL_TOKEN = os.environ.get("INFISICAL_TOKEN")

client = InfisicalClient(site_url=INFISICAL_API_URL, token=INFISICAL_TOKEN)


@app.route("/")
def hello_world():
    name = client.get_secret(secret_name="NAME", environment="dev", type="shared")
    return f"Hello! My name is: {name.secret_value}"


if __name__ == "__main__":
    app.run(debug=True)
