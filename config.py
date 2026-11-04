import os
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger("opencut.config")

class Config:
    """Gerenciamento de configurações centralizado para o OpenCut."""
    BASE_DIR: Path = Path(__file__).resolve().parent
    OUTPUT_DIR: Path = BASE_DIR / "output"
    TEMP_DIR: Path = BASE_DIR / "temp"
    
    # Configurações de IA e Processamento
    DEFAULT_MODEL: str = os.getenv("OPENCUT_MODEL", "qwen2.5-coder:1.5b")
    OLLAMA_HOST: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    
    @classmethod
    def initialize(cls) -> None:
        """Garante que os diretórios essenciais existam."""
        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        cls.TEMP_DIR.mkdir(parents=True, exist_ok=True)
        logger.info(f"Diretórios base inicializados: {cls.OUTPUT_DIR}, {cls.TEMP_DIR}")

if __name__ == "__main__":
    Config.initialize()
    logger.info(f"Configurações carregadas. Modelo padrão: {Config.DEFAULT_MODEL}")
