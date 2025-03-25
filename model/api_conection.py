import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class AIService:
    def __init__(self):
        # Configuração inicial com a chave da OpenAI
        self.client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url="https://api.deepseek.com")
        self.default_model = "deepseek-chat"
        self.system_prompt = """
        Você é um assistente IA útil. Responda de forma clara e concisa,
        mantendo um tom profissional e amigável.
        """

    def generate_response(self, user_input: str, system_prompt: str = None) -> str:
        """Gera uma resposta do modelo de linguagem com base na entrada do usuário.
        
        Args:
            user_input (str): Texto de entrada do usuário
            system_prompt (str, optional): Prompt personalizado. Defaults para o prompt padrão.
        
        Returns:
            str: Resposta gerada pelo modelo
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.default_model,
                messages=[
                    {"role": "system", "content": system_prompt or self.system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Erro ao processar a requisição: {str(e)}"

# Instância singleton para ser usada na aplicação
ai_service = AIService()