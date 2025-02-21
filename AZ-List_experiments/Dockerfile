# Usando uma imagem base oficial do Python
FROM python:3.11-slim

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando os arquivos necessários
COPY list_experiments.py requirements.txt config.json ./

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão de execução do container
CMD ["python", "list_experiments.py"]
