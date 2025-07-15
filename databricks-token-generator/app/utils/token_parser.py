"""
Filename: token_parser.py
Author: Jean Alves
Created on: 2025-07-15
Description: Utility functions for parsing access tokens from PowerShell script outputs
             and handling token-related operations.
"""

import re
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

