from azureml.core import Workspace, Run

# Conectar ao workspace
ws = Workspace.from_config()

# Recuperar o job pelo run_id
run_id = "eac6cdf9-3eb0-40e8-97cb-311a38f51b36"
run = Run.get(ws, run_id)

# Obter detalhes da imagem usada
image_details = run.get_details().get("properties", {}).get("azureml.container_image")
print(f"Imagem usada no job: {image_details}")
