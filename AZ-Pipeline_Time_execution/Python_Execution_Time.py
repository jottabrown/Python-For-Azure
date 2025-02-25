import requests
import base64
import json
from datetime import datetime, timezone
import statistics


with open("config_time.json", "r") as config_file:
    config = json.load(config_file)

organization = config["organization"]
project = config["project"]
pipeline_id = config["pipeline_id"]
personal_access_token = config["personal_access_token"]

# URL da API para listar todas as pipelines
url_pipelines = f"https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=7.1-preview.1"

# Autenticação Base64
auth_header = base64.b64encode(f":{personal_access_token}".encode()).decode()
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json"
}

# Função para converter a data com diferentes formatos possíveis
def parse_datetime(date_str):
    """ Converte a string de data para datetime, tratando diferentes formatos. """
    date_str = date_str.rstrip("Z")  # Remove o "Z" no final

    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):  # Com e sem microssegundos
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Formato de data desconhecido: {date_str}")

# Requisição para listar todas as pipelines
response_pipelines = requests.get(url_pipelines, headers=headers)

if response_pipelines.status_code != 200:
    print(f"Erro na API: {response_pipelines.status_code} - {response_pipelines.text}")
    exit()

try:
    pipelines_data = response_pipelines.json()
except requests.exceptions.JSONDecodeError:
    print("Erro ao decodificar JSON. Resposta da API:", response_pipelines.text)
    exit()

# Se não houver pipelines
if "value" not in pipelines_data or not pipelines_data["value"]:
    print("Nenhuma pipeline encontrada.")
    exit()

# Define a data de hoje para comparação
today = datetime.now(timezone.utc).date()


# Variáveis para calcular as métricas
durations = []
frequency = 0

# Para cada pipeline, pegar as execuções
for pipeline in pipelines_data["value"]:
    pipeline_id = pipeline["id"]
    print(f"Analisando pipeline ID: {pipeline_id}")

    # URL para pegar as execuções de cada pipeline
    url_runs = f"https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1"
    
    # Requisição para pegar as execuções da pipeline
    response_runs = requests.get(url_runs, headers=headers)

    if response_runs.status_code != 200:
        print(f"Erro na API para pipeline ID {pipeline_id}: {response_runs.status_code} - {response_runs.text}")
        continue

    try:
        runs_data = response_runs.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Erro ao decodificar JSON para pipeline ID {pipeline_id}. Resposta: {response_runs.text}")
        continue

    # Processar execuções da pipeline
    if "value" in runs_data and runs_data["value"]:
        for run in runs_data["value"]:
            if "createdDate" in run and "finishedDate" in run:
                try:
                    start_time = parse_datetime(run["createdDate"])
                    finish_time = parse_datetime(run["finishedDate"])

                    # Verifica se a execução é de hoje
                    if start_time.date() == today:
                        duration = (finish_time - start_time).total_seconds() / 60  # Minutos
                        durations.append(duration)
                        frequency += 1
                except ValueError as e:
                    print(f"Erro ao processar datas para a execução da pipeline ID {pipeline_id}: {e}")

# Calcula a média de duração
if durations:
    avg_duration = statistics.mean(durations)
    print(f"Média de execução de todas as pipelines: {avg_duration:.2f} minutos")
else:
    print("Nenhuma execução válida encontrada para hoje.")

# Exibe a frequência de execuções
print(f"Frequência de execuções hoje: {frequency}")