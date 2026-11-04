import subprocess
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger("opencut.video_processor")

class VideoProcessor:
    """Gerencia operações de manipulação de vídeo utilizando FFmpeg."""
    
    @staticmethod
    def run_ffmpeg_command(cmd: list[str]) -> bool:
        """Executa um comando FFmpeg com tratamento robusto de erros e logs."""
        logger.info(f"Executando comando: {' '.join(cmd)}")
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            logger.info("Comando FFmpeg executado com sucesso.")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Erro ao executar FFmpeg (código {e.returncode}): {e.stderr.strip()}")
            return False
        except FileNotFoundError:
            logger.error("FFmpeg não encontrado no sistema. Verifique se está instalado e no PATH.")
            return False

    @classmethod
    def get_video_info(cls, input_path: Path) -> str:
        """Retorna informações básicas do arquivo de vídeo."""
        cmd = ["ffprobe", "-v", "error", "-show_format", "-show_streams", str(input_path)]
        logger.info(f"Coletando metadados do vídeo: {input_path}")
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout
        except Exception as e:
            logger.error(f"Erro ao obter informações do vídeo: {e}")
            return ""

if __name__ == "__main__":
    logger.info("Módulo VideoProcessor carregado com sucesso.")
