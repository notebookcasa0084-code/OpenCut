import os
import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)

class AudioExtractor:
    def __init__(self, output_dir: str = "temp"):
        """
        Inicializa o extrator de áudio definindo o diretório de saída para arquivos temporários.
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract_audio(self, video_path: str, output_audio_name: str = "extracted_audio.mp3") -> str:
        """
        Extrai o áudio de um arquivo de vídeo utilizando ffmpeg.
        Retorna o caminho completo para o arquivo de áudio gerado.
        """
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Arquivo de vídeo não encontrado: {video_path}")

        output_path = self.output_dir / output_audio_name
        
        cmd = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-vn",
            "-acodec", "libmp3lame",
            "-ar", "16000",
            "-ac", "1",
            str(output_path)
        ]

        logger.info(f"Extraindo áudio do vídeo {video_path} para {output_path}...")
        
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            logger.info("Áudio extraído com sucesso.")
            return str(output_path)
        except subprocess.CalledProcessError as e:
            logger.error(f"Erro no ffmpeg ao extrair áudio: {e.stderr}")
            raise RuntimeError(f"Falha na extração de áudio: {e.stderr}")
