"""
Compare Azure Key Vault VS Infisical speed
"""
import os
import time
from azure.identity import DefaultAzureCredential, EnvironmentCredential, CredentialUnavailableError
from azure.keyvault.secrets import SecretClient
from infisical import InfisicalClient

AZURE_KEYVAULT_URL = os.getenv("AZURE_KEYVAULT_URL")
INFISICAL_API_URL = os.environ.get("INFISICAL_API_URL")
INFISICAL_TOKEN = os.environ.get("INFISICAL_TOKEN")
ITERATION = 10


def get_azure_credential():
    """Get Azure credential"""
    try:
        credential = DefaultAzureCredential()
    except CredentialUnavailableError:
        credential = EnvironmentCredential()
    return credential


def get_azure_keyvault_secret(name):
    """Get Azure keyvault secret"""
    credential = get_azure_credential()
    client = SecretClient(vault_url=AZURE_KEYVAULT_URL, credential=credential)
    return client.get_secret(name)

def get_infisical_secret(name):
    client = InfisicalClient(site_url=INFISICAL_API_URL, token=INFISICAL_TOKEN)
    return client.get_secret(secret_name=name, environment="dev", type="shared")
    


if __name__ == "__main__":
    total_start = time.time()
    for _ in range(ITERATION):
        start = time.time()
        secret = get_azure_keyvault_secret(name="secret-to-compare")
        print(f"Time to get secret from Azure Key Vault: {time.time() - start}")
    print(f"Total time to get secret from Azure Key Vault: {time.time() - total_start}")
    
    total_start = time.time()
    for _ in range(ITERATION):
        start = time.time()
        secret = get_infisical_secret(name="SECRET_TO_COMPARE")
        print(f"Time to get secret from Infisical: {time.time() - start}")
    print(f"Total time to get secret from Infisical: {time.time() - total_start}")
    
