import streamlit as st
import sys
from pathlib import Path
# Adicione o diretório raiz ao PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))
from llm_services.llm_client import ai_service


def main():
    # Configuração da página
    st.set_page_config(
        page_title="AI Agent Interface",
        page_icon="🤖",
        layout="wide"
    )

    # Título principal
    st.title("Bem-vindo ao Assistente IA! 🤖")
    
    # Subtítulo
    st.markdown("### Esta é uma interface para interagir com um agente de IA")
    
    # Área de texto para input do usuário
    user_input = st.text_area("Digite sua mensagem:", height=150)
    
    # Botão de envio
    if st.button("Enviar"):
        if user_input:
            with st.spinner("Processando sua solicitação..."):
                response = deepseek_service.chat_completion(user_input)
                st.write("Resposta do Assistente:")
                st.success(response)
        else:
            st.warning("Por favor, digite uma mensagem antes de enviar.")

if __name__ == "__main__":
    main()