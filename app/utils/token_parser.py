import re
import subprocess
from typing import Optional


def extract_token_from_output(output: str) -> Optional[str]:
    """
    Extrai o token da saída padrão do script PowerShell.
    
    Args:
        output (str): Texto da saída padrão do script PowerShell.

    Returns:
        str | None: O token extraído, ou None se não encontrado.
    """
    match = re.search(r'Token:\s*(.+)', output)
    if match:
        return match.group(1).strip()
    return None

def run_powershell_script(script_path, args):
    cmd = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", str(script_path)] + args
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout