import os
from infisical import InfisicalClient

INFISICAL_API_URL = os.environ.get("INFISICAL_API_URL")
INFISICAL_TOKEN = os.environ.get("INFISICAL_TOKEN")

client = InfisicalClient(site_url=INFISICAL_API_URL, token=INFISICAL_TOKEN)
secret = client.get_secret(secret_name="DATABASE_URL", environment="dev", type="shared")
secrets = client.get_all_secrets()

print(f"DATABASE_URL: {secret.secret_value}")
for secret in secrets:
    print(f"{secret.secret_name}: {secret.secret_value}")
