"""
Filename: azure_cli.py
Author: Jean Alves
Created on: 2025-07-15
Description: Functions to interact with Azure CLI and extract metadata related to Service Principals,
             such as tenant ID, client ID, etc.
"""


import subprocess
import json

def get_sp_info_from_azure(sp_name: str) -> dict:
    # Caminho absoluto do executável az.cmd
    AZ_PATH = r"C:\Program Files (x86)\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"

    try:
        result = subprocess.run(
            [AZ_PATH, "ad", "sp", "show", "--id", sp_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        sp_data = json.loads(result.stdout)
        return {
            "tenant_id": sp_data["appOwnerTenantId"],
            "client_id": sp_data["appId"],
            "scope": "https://management.azure.com/.default"
        }

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao buscar SP no Azure CLI:\n{e.stderr or e.stdout}")
    except FileNotFoundError:
        raise RuntimeError("❌ Azure CLI (az.cmd) não encontrado. Verifique o caminho no código.")
    except Exception as e:
        raise RuntimeError(f"❌ Erro inesperado: {str(e)}")