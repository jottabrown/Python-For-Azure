import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Carregar as configurações do arquivo JSON
with open("config.json", "r") as file:
    config = json.load(file)

# Obter o nome do Key Vault de destino a partir do config.json
destination_kv_name = config["destination_key_vault"]
destination_kv_url = f"https://{destination_kv_name}.vault.azure.net/"
credential = DefaultAzureCredential()

# Conectar ao Key Vault de destino
destination_client = SecretClient(vault_url=destination_kv_url, credential=credential)

# Função para listar as secrets no Key Vault de destino
def listar_secrets():
    secrets = destination_client.list_properties_of_secrets()  # Listar as propriedades das secrets
    return [secret.name for secret in secrets]  # Retorna apenas os nomes das secrets

# Validação das secrets migradas
def validar_secrets(secret_names):
    secrets_destino = listar_secrets()  # Lista todas as secrets do Key Vault de destino

    for secret_name in secret_names:
        if secret_name in secrets_destino:
            print(f"✅ Secret '{secret_name}' está presente no Key Vault de destino.")
        else:
            print(f"⚠️ Secret '{secret_name}' NÃO está presente no Key Vault de destino.")

# Lista de secrets que foram migradas (substitua pelos nomes das suas secrets)
secret_names_migradas = config["secrets"]

# Executa a validação
validar_secrets(secret_names_migradas)
