"""
Filename: powershell_runner.py
Author: Jean Alves
Created on: 2025-07-15
Description:
    Utility functions to execute PowerShell scripts from Python using subprocess,
    handle arguments, and capture output for token processing or other automation tasks.

Usage:
    run_powershell_script(script_path, arguments_list)
"""

import subprocess

def run_powershell_script(script_path, args):
    cmd = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", str(script_path)] + args
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout