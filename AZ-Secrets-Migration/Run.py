import json
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from tqdm import tqdm  # Importando a barra de progresso

# Carregar as configurações do arquivo JSON
with open("config.json", "r") as file:
    config = json.load(file)

# Extrair informações do arquivo de configuração
workspaces = config["workspaces"]
secret_names = config["secrets"]
destination_kv_name = config["destination_key_vault"]
credential = DefaultAzureCredential()

# Função para buscar o segredo em todos os workspaces
def buscar_secret(secret_name):
    for workspace in workspaces:
        key_vault_name = workspace["key_vault_name"]
        kv_url = f"https://{key_vault_name}.vault.azure.net/"
        client = SecretClient(vault_url=kv_url, credential=credential)
        
        try:
            return client.get_secret(secret_name).value  # Retorna o valor do segredo
        except Exception:
            continue  # Caso não encontre, tenta o próximo workspace

    return None  # Retorna None se o segredo não for encontrado em nenhum workspace

# Conectar ao Key Vault de destino
destination_kv_url = f"https://{destination_kv_name}.vault.azure.net/"
destination_client = SecretClient(vault_url=destination_kv_url, credential=credential)

# Barra de progresso para iterar sobre os secrets
for secret_name in tqdm(secret_names, desc="Migrando secrets", unit="secret"):
    secret_value = buscar_secret(secret_name)
    
    if secret_value:  # Se o segredo for encontrado
        destination_client.set_secret(secret_name, secret_value)  # Armazenar no Key Vault de destino
        print(f"✅ Secret '{secret_name}' migrada para {destination_kv_name}")
    else:
        print(f"⚠️ Secret '{secret_name}' não encontrada nos Key Vaults de origem.")
