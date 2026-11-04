import sys
from pathlib import Path
from config import Config
from utils.logger import setup_logger
from utils.video_processor import VideoProcessor
from utils.ai_client import OllamaClient

logger = setup_logger("opencut.main")

def main():
    logger.info("=== Iniciando o OpenCut ===")
    
    # 1. Inicializar diretórios e configurações
    Config.initialize()
    logger.info(f"Modelo de IA configurado: {Config.DEFAULT_MODEL}")
    
    # 2. Inicializar clientes
    ai_client = OllamaClient()
    
    # 3. Exemplo de uso integrado (opcional / demonstração)
    logger.info("Verificando dependências e ambiente...")
    
    # Teste rápido de IA se solicitado ou demonstrativo
    test_prompt = "Responda em uma frase: O OpenCut está pronto para edição automatizada de vídeo?"
    ai_response = ai_client.generate(test_prompt, system_prompt="Você é um assistente de engenharia de vídeo profissional.")
    logger.info(f"Resposta de teste da IA: {ai_response}")
    
    logger.info("=== OpenCut executado com sucesso ===")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f crítico não tratado no main: {e}")
        sys.exit(1)
