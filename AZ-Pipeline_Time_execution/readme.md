# Azure Pipeline Metrics Analyzer

Este script permite obter e analisar métricas de execução de pipelines no Azure DevOps, incluindo a duração média das execuções e a frequência de execuções no dia atual.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos:

- Python 3.x instalado
- Bibliotecas Python:
  - `requests`
  - `base64`
  - `json`
  - `datetime`
  - `statistics`

Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash
    pip install requests
```


## Instalação das Dependências

Antes de executar o script, é necessário instalar as dependências do projeto. Para isso, siga os passos abaixo:

1. Crie e ative o ambiente virtual (venv):

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Instale as dependências a partir do arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt


## Configuração do Arquivo `config_time.json`

Antes de rodar o script, você precisa configurar o arquivo `config_time.json` com as informações abaixo:

- **organization**: Nome da sua organização no Azure DevOps.
- **project**: Nome do projeto dentro da organização.
- **pipeline_id**: ID da pipeline a ser analisada.
- **personal_access_token**: Token de acesso pessoal (PAT) do Azure DevOps.

Aqui está um exemplo de como deve ser o seu arquivo `config_time.json`:

```json
{
  "organization": "your_organization",
  "project": "your_project",
  "pipeline_id": "your_pipeline_id",
  "personal_access_token": "your_personal_access_token"
}
```
## Como Funciona? 🤔

O script segue as seguintes etapas para analisar e gerar as métricas de execução da pipeline:

1. **Carrega as Configurações 📂**  
   O script começa lendo o arquivo `config_time.json` para obter as informações necessárias para autenticação e configuração da pipeline. As informações incluem:
   - Organização no Azure DevOps
   - Nome do projeto
   - ID da pipeline
   - Token de acesso pessoal (PAT)

2. **Acessa a API do Azure DevOps 🌐**  
   Utiliza a API do Azure DevOps para buscar todas as pipelines no projeto especificado e obter detalhes sobre suas execuções.

3. **Obtenção de Execuções 📊**  
   Para cada pipeline identificada, o script acessa as execuções realizadas, analisando a data de criação e finalização de cada uma. Isso permite um controle detalhado sobre os momentos em que as execuções ocorreram.

4. **Calcula Métricas 📈**  
   O script calcula duas métricas principais:
   - **Média de Duração ⏳**: Calcula a média de tempo de execução das pipelines que ocorreram no **dia atual**.
   - **Frequência de Execuções 🔄**: Conta o número de execuções realizadas ao longo do **dia atual**.

Essas métricas são essenciais para otimizar o processo de execução das pipelines e ajudar na análise de desempenho e uso de recursos.


## Como Executar 🚀

Para rodar o script, basta executar o comando Python diretamente:

```bash
python azure_pipeline_metrics.py
``` 
## Como Executar via Docker 🐳

Para rodar o script dentro de um container Docker, siga os passos abaixo:

1. **Clone o repositório** (caso ainda não tenha feito):

    ```bash
    git clone https://github.com/seuusuario/Python-For-Azure.git
    ```

2. **Navegue até a pasta do projeto**:

    ```bash
    cd Python-For-Azure
    ```

3. **Construa a imagem Docker**:

    No terminal, execute o comando para construir a imagem Docker:

    ```bash
    docker build -t azure-pipeline-metrics .
    ```

4. **Execute o container**:

    Após a imagem ser construída, execute o script dentro do container:

    ```bash
    docker run --rm azure-pipeline-metrics
    ```

    O script será executado no container e, ao final, o container será removido automaticamente.

Agora você pode rodar o script facilmente em qualquer ambiente isolado usando o Docker! 🔥🚀

## Exemplo de Saída 🖥️

Ao executar o script, você verá a saída com as métricas das pipelines analisadas:

```bash 
Analisando pipeline ID: 1
Média de execução de todas as pipelines: 15.30 minutos
Frequência de execuções hoje: 3
``` 

## Contribuições 💡

Contribuições são sempre bem-vindas! Se você tem sugestões, melhorias ou correções, por favor, faça um fork do repositório e envie um pull request.