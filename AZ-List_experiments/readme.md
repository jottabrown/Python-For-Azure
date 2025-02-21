# AZ-List_experiments

## Descrição
Este script lista experimentos do Azure Machine Learning filtrados de acordo com um arquivo de configuração (`config.json`). Para cada experimento listado, exibe-se o nome e a data da última execução.

## Estrutura do Projeto
```
AZ-List_experiments/
│-- list_experiments.py
│-- config.json
│-- requirements.txt
│-- Dockerfile
│-- README.md
```

## Configuração
O script depende de um arquivo `config.json`, que deve conter as seguintes informações:
```json
{
  "workspace_name": "SEU_WORKSPACE",
  "subscription_id": "SUA_SUBSCRIPTION_ID",
  "resource_group": "SEU_RESOURCE_GROUP",
  "experimentos": [
    "experimento1",
    "experimento2",
    "experimento2",
    "experimento3",
    "experimento5",
    "experimento6",
    "experimento7",
    "experimento8",
    "experimento9"
  ]
}
```

## Instalação
1. Clone o repositório e entre na pasta `AZ-List_experiments`:
   ```sh
   git clone <seu-repositorio>
   cd AZ-List_experiments
   ```
2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso
Execute o script com:
```sh
python list_experiments.py
```

## Dockerização
### Construção da Imagem
```sh
docker build -t az-list-experiments .
```

### Execução do Container
```sh
docker run --rm -v $(pwd)/config.json:/app/config.json az-list-experiments
```

## Autor
**Jean Alves**
- LinkedIn: [Jean Alves](https://www.linkedin.com/in/jean-alves-6671a7105/)
- Email: jeancleber.alves@hotmail.com
