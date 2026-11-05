import logging
from faster_whisper import WhisperModel

logger = logging.getLogger(__name__)

class AudioTranscriber:
    def __init__(self, model_size: str = "base", device: str = "cpu", compute_type: str = "int8"):
        self.model_size = model_size
        self.device = device
        self.compute_type = compute_type
        logger.info(f"Carregando o modelo Whisper ({model_size}) no dispositivo {device}...")
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)

    def transcribe(self, audio_path: str) -> str:
        try:
            logger.info(f"Iniciando transcrição para o arquivo: {audio_path}")
            segments, info = self.model.transcribe(audio_path, beam_size=5)
            
            transcript_text = ""
            for segment in segments:
                transcript_text += segment.text + " "
                
            logger.info(f"Transcrição concluída com sucesso. Idioma detectado: {info.language} (probabilidade: {info.language_probability:.2f})")
            return transcript_text.strip()
        except Exception as e:
            logger.error(f"Erro durante a transcrição do áudio: {e}")
            raise e
