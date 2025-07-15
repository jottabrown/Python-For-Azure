# 🔐 Databricks Token Generator

Projeto em Python com interface Streamlit para gerar tokens de acesso ao Databricks usando autenticação via Azure Service Principal. Automatiza a geração dos tokens executando scripts PowerShell que interagem com APIs do Azure e Databricks.

---

## 🧩 Visão Geral

Este projeto facilita a criação de tokens de acesso ao Azure Databricks de forma simples e segura, usando uma interface web leve construída com Streamlit. Ele automatiza as chamadas para geração do token via scripts PowerShell e exibe o token na tela com opção de cópia rápida.

---

## 🚀 Funcionalidades

- Interface web intuitiva para preencher credenciais e parâmetros do token.
- Execução automática de scripts PowerShell para autenticação e geração do token.
- Extração do token da saída dos scripts usando expressões regulares.
- Exibição do token gerado com botão para copiar para a área de transferência.
- Validação dos campos e tratamento de erros com mensagens amigáveis.

---

## 📁 Estrutura do Projeto

```
databricks-token-generator/
├── app/
│   ├── __init__.py
│   ├── main.py              # Código principal da aplicação Streamlit
│   ├── ui/
│   │   └── logo.png         # Logo para exibir na interface
│   ├── scripts/
│   │   ├── token.ps1        # Script PowerShell para autenticação no Azure
│   │   └── token2.ps1       # Script PowerShell para geração do token Databricks
│   └── utils/
│       ├── token_parser.py  # Funções utilitárias, regex para extrair token, execução dos scripts
├── start.bat # Script para iniciar a aplicação no Windows
├── requirements.txt         # Dependências Python
├── README.md
└── .gitignore
```

---

## 💻 Como usar

### Pré-requisitos

- Python 3.8+
- PowerShell instalado e disponível no PATH
- Ambiente virtual Python (recomendado)
- Scripts PowerShell com permissões adequadas

### Passos

1. Clone este repositório:

```
git clone https://github.com/jottabrown/Python-For-Azure.git
cd databricks-token-generator/app
```

2. Crie e ative um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\Activate.ps1 # Windows PowerShell
.\venv\Scripts\activate.bat # Windows CMD
```

3. Instale as dependências:

```
pip install -r ../requirements.txt
```

4. Execute a aplicação Streamlit:

```
streamlit run main.py ou execute o start.bat
```

5. Preencha os campos solicitados (Tenant ID, Client ID, Client Secret, etc.) e clique em **Gerar Tokens**.

6. O token gerado aparecerá na tela com botão para copiar.

---

## 🔧 Personalização

- Atualize os scripts PowerShell em `app/scripts/` conforme necessidade.
- Modifique a interface em `app/main.py` para incluir novos parâmetros ou validações.
- Adicione loggers ou outras funções utilitárias em `app/utils/token_parser.py`.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- PowerShell
- Expressões regulares para extração de dados
- subprocess para execução dos scripts

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 📫 Contato

Para dúvidas, sugestões ou contribuições, abra uma issue ou envie um e-mail para jeancleber.alves@hotmail.com

---

## 📢 Agradecimentos

Obrigado por usar e contribuir com este projeto! 🚀
