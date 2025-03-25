import streamlit as st
import sys
from pathlib import Path
import uuid
from loguru import logger
# Adicione o diretório raiz ao PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))
from llm_services.deepseek_client import deepseek_service


def main():
    # Configuração da página
    st.set_page_config(
        page_title="AI Agent Interface",
        page_icon="🤖",
        layout="wide"
    )
    # Inicialização do estado da sessão, se necessário
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = {}

    if 'current_chat_id' not in st.session_state:
        st.session_state.current_chat_id = str(uuid.uuid4())
        st.session_state.chat_history[st.session_state.current_chat_id] = []

    # Função para criar um novo chat
    def create_new_chat():
        st.session_state.current_chat_id = str(uuid.uuid4())
        st.session_state.chat_history[st.session_state.current_chat_id] = []
    
    # Sidebar
    with st.sidebar:
        st.title("Configurações do Chat")
        
        # Exibir o modelo atual
        st.subheader("Modelo Atual")
        current_model = deepseek_service.default_model
        st.info(f"Usando: {current_model}")
        
        # Botão para criar novo chat
        if st.button("Novo Chat", key="new_chat"):
            create_new_chat()
        
        # Lista de chats existentes
        st.subheader("Seus Chats")
        for chat_id in st.session_state.chat_history:
            # Cria um nome curto para o chat baseado nos primeiros caracteres do ID
            chat_name = f"Chat {chat_id[:6]}..."
            if st.button(chat_name, key=f"select_{chat_id}"):
                st.session_state.current_chat_id = chat_id

    # Área principal do chat
    st.title("Bem-vindo ao Assistente IA! 🤖")

    # Subtítulo
    st.markdown("### Esta é uma interface para interagir com um agente de IA")
    
    # Exibir histórico do chat atual
    current_chat = st.session_state.chat_history[st.session_state.current_chat_id]
    for message in current_chat:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])
    
    # Input para nova mensagem
    user_input = st.chat_input("Digite sua mensagem aqui...")
    if user_input:
        # Adicionar mensagem do usuário ao histórico
        st.chat_message("user").write(user_input)
        current_chat.append({"role": "user", "content": user_input})
        
        logger.debug("Estado do chat antes da requisição:")  
        for idx, msg in enumerate(current_chat):  
            logger.debug("Mensagem {}: {}", idx, msg)

        # Obter resposta da API
        response = deepseek_service.chat_completion(current_chat)
        
        # Adicionar resposta ao histórico
        st.chat_message("assistant").write(response)
        current_chat.append({"role": "assistant", "content": response})
        
        # Atualizar o histórico na sessão
        st.session_state.chat_history[st.session_state.current_chat_id] = current_chat

if __name__ == "__main__":
    main()