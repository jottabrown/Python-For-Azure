import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from utils.token_parser import extract_token_from_output, run_powershell_script

import subprocess

logo_path = Path(__file__).parent / "ui" / "logo.png"

# Cabeçalho com logo centralizado e estilizado
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image(str(logo_path), width=100)
with col_title:
    st.markdown("""
        <h1 style='
            font-size: 28px;
            padding-top: 20px;
            font-weight: 600;
            color: white;
        '>
        🔐 Gerador de Token SP Databricks
        </h1>
    """, unsafe_allow_html=True)

tenant_id = st.text_input("Tenant ID")
client_id = st.text_input("Client ID")
client_secret = st.text_input("Client Secret", type="password")
scope = st.text_input("Scope", value="escope do sp/.default")

databricksHost = st.text_input("Databricks Host", value="https://adb-xxxxxxx.azuredatabricks.net")
application_id = st.text_input("Application ID")  # sem valor default para evitar confusão

dias = st.text_input("Validade do token (dias)", value="90")
comentario = st.text_input("Comentário do token", value="Token gerado")

if st.button("🚀 Gerar Tokens"):
    if not tenant_id or not client_id or not client_secret or not databricksHost or not application_id:
        st.error("❗ Por favor, preencha todos os campos obrigatórios.")
    else:
        try:
            dias_int = int(dias)
        except ValueError:
            st.error("❗ 'Validade do token' deve ser um número.")
            dias_int = None

        if dias_int is not None:
            base_dir = Path(__file__).parent
            scripts_dir = base_dir / "scripts"
            token_script = scripts_dir / "token.ps1"
            token2_script = scripts_dir / "token2.ps1"

            if not token_script.exists() or not token2_script.exists():
                st.error("⚠️ Scripts PowerShell não encontrados no diretório 'scripts'.")
            else:
                args_token = [
                    "-tenantId", tenant_id,
                    "-clientId", client_id,
                    "-clientSecret", client_secret,
                    "-scope", scope
                ]

                args_token2 = [
                    "-databricksHost", databricksHost,
                    "-applicationId", application_id,
                    "-dias", str(dias_int),
                    "-comentario", comentario
                ]

                try:
                    with st.spinner("⏳ Gerando token, aguarde..."):
                        # Executa o primeiro script (sem saída capturada)
                        run_powershell_script(token_script, args_token)

                        # Executa o segundo script e captura a saída
                        output = run_powershell_script(token2_script, args_token2)

                    token_value = extract_token_from_output(output)

                    if token_value:
                        st.success("✅ Token gerado com sucesso!")
                        st.markdown("### 🔐 Seu token gerado é:")
                        st.code(token_value)

                        components.html(f"""
                            <button onclick="navigator.clipboard.writeText(`{token_value}`)"
                                    style="
                                        background-color: #1f77b4;
                                        color: white;
                                        border: none;
                                        padding: 10px 20px;
                                        margin-top: 10px;
                                        font-size: 16px;
                                        border-radius: 6px;
                                        cursor: pointer;">
                                📋 Copiar token para a área de transferência
                            </button>
                        """, height=60)
                    else:
                        st.warning("⚠️ Token gerado, mas não foi possível extrair o valor da saída.")
                        st.code(output)

                except subprocess.CalledProcessError as e:
                    st.error("❌ Erro ao gerar tokens:")
                    st.code(e.stderr or e.output or str(e))
