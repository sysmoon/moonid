from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

CLIENT_ID = 'e69a5858-7f0d-49da-9246-e377312eed9a'
SECRET = 'rO72ChdsTpUotM/cGi6PzL18UasSelCWgRd/7MvG92c='
TENANT = '344a52e5-db8e-48e7-80ca-5f73722ac6aa'
VAULT_URL = "https://moonid.vault.azure.net"
SECRET_VERSION = 'b247ec811cae40dabead03ea0eeb1632'

def getKVClient():
    credential = ServicePrincipalCredentials(
        client_id = CLIENT_ID,
        secret = SECRET,
        tenant = TENANT
    )
    client = KeyVaultClient(credential)

    return client


def getKVByKey(key):
    global SERCRET
    client = getKVClient()
    secret = client.get_secret(VAULT_URL, key, SECRET_VERSION)

    print(secret)

def setKV(key, name):
    credential = getKVCrendential()

if __name__ == '__main__':
    getKVByKey('testkey')