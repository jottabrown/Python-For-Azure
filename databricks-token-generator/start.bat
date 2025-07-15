@echo off
echo.
echo ================================
echo Ativando ambiente virtual...
echo ================================
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo Ambiente virtual ativado com sucesso!
    echo Versao do Python em uso:
    python --version
    where python
) else (
    echo ERRO: Ambiente virtual nao encontrado em "venv\".
    echo Execute: python -m venv venv
    pause
    exit /b
)

echo.
echo ================================
echo Iniciando Streamlit App...
echo ================================
streamlit run app\main.py

echo.
pause
