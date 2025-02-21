#---------------------------------------------------------------------------------------
# Author: Jean Alves
# Position: Systems Analyst | Software Engineer | Machine Learning Engineer
# Email: jeancleber.alves@hotmail.com
# LinkedIn: https://www.linkedin.com/in/jean-alves-6671a7105/
#---------------------------------------------------------------------------------------

import json
import os
import time
from datetime import datetime
from azureml.core import Workspace
from azureml.core.authentication import AzureCliAuthentication

# Início da contagem do tempo
start_time = time.time()

# Caminho para o arquivo de configuração (config.json)
config_file_path = './config.json'

# Verificando se o arquivo de configuração existe
if not os.path.exists(config_file_path):
    raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_file_path}")

# Carregar o arquivo JSON
with open(config_file_path) as f:
    config = json.load(f)
    experimentos_desejados = set(config["experimentos"])  # Usando set para otimizar buscas

# Autenticação e obtenção do workspace
ws = Workspace.get(
    name=config['workspace_name'],
    subscription_id=config['subscription_id'],
    resource_group=config['resource_group'],
    auth=AzureCliAuthentication()
)

# Listar experimentos e exibir detalhes
print("\n📌 Experimentos encontrados:")
print("-" * 80)

for name, experiment in ws.experiments.items():
    if name in experimentos_desejados:
        last_run = next(experiment.get_runs(), None)  # Obtém o primeiro run (última execução)
        
        last_run_time = "Nenhuma execução encontrada"
        run_id = "N/A"
        status = "Desconhecido"
        created_by = "Desconhecido"

        if last_run:
            run_details = last_run.get_details()
            run_id = last_run.id
            status = run_details.get("status", "Desconhecido")
            created_by = run_details.get("createdBy", {}).get("userName", "Desconhecido")

            if "startTimeUtc" in run_details:
                last_run_time = datetime.strptime(run_details["startTimeUtc"], "%Y-%m-%dT%H:%M:%S.%fZ")

        # Exibir detalhes formatados
        print(f"🔹 Nome: {name}")
        print(f"   📅 Última execução: {last_run_time}")
        print(f"   🔄 Status: {status}")
        print(f"   🆔 Run ID: {run_id}")
        print(f"   👤 Criado por: {created_by}")
        print("-" * 80)

# Tempo total de execução
end_time = time.time()
print(f"\n⏳ Tempo total de execução: {round(end_time - start_time, 2)} segundos")
