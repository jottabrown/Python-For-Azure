# Python-For-Azure

Este repositório contém uma coleção de scripts em Python para gerenciamento e suporte de ambientes Azure. Os scripts são projetados para automatizar tarefas comuns, como listar schedules, gerenciar recursos, entre outros, no Azure.

Cada script está contido em uma pasta individual, que inclui um README explicativo sobre o funcionamento do script, além de um Dockerfile para facilitar a execução em ambientes isolados.

## Funcionalidades

- **Gerenciamento de Schedules**: Scripts para listar, modificar e remover schedules no Azure.
- **Gerenciamento de Recursos**: Scripts para controlar e verificar status de recursos no Azure.
- **Automação**: Facilita a automação de tarefas diárias no ambiente Azure com Python.

## Como Usar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/Python-For-Azure.git
    ```

2. Navegue até a pasta do script desejado:

    ```bash
    cd script_1
    ```

3. Leia o README dentro de cada pasta para detalhes sobre como executar o script e configurar o ambiente.

4. Se necessário, construa a imagem Docker para execução do script:

    ```bash
    docker build -t nome_da_imagem .
    ```

5. Execute o script (caso não esteja usando Docker, basta rodar o script diretamente com Python):

    ```bash
    python script.py
    ```

## Contribuindo

Se você deseja contribuir para o repositório, faça um fork e envie um pull request com suas melhorias.

## Licença

Este repositório é licenciado sob a [MIT License](LICENSE).
