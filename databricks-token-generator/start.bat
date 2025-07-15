@echo off
echo 🟢 Ativando o ambiente virtual...
call app\venv\Scripts\activate.bat

echo 🚀 Iniciando o app Streamlit...
streamlit run app\main.py

pause