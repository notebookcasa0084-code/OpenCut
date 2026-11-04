import requests
from config import Config
from utils.logger import setup_logger

logger = setup_logger("opencut.ai_client")

class OllamaClient:
    """Cliente para comunicação com o Ollama e modelos locais de IA."""
    
    def __init__(self, host: str = Config.OLLAMA_HOST, model: str = Config.DEFAULT_MODEL):
        self.host = host.rstrip("/")
        self.model = model
        self.api_url = f"{self.host}/api/generate"
        logger.info(f"OllamaClient inicializado (Host: {self.host}, Modelo: {self.model})")

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        """Envia um prompt para o modelo local e retorna a resposta gerada."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        if system_prompt:
            payload["system"] = system_prompt

        logger.info(f"Enviando requisição para o Ollama (modelo: {self.model})...")
        try:
            response = requests.post(self.api_url, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            result = data.get("response", "")
            logger.info("Resposta recebida com sucesso do Ollama.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro de comunicação com o Ollama: {e}")
            return f"[Erro na IA: {e}]"

if __name__ == "__main__":
    client = OllamaClient()
    logger.info("Módulo OllamaClient carregado e pronto para uso.")
