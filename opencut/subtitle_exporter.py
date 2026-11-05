import logging
from pathlib import Path
from typing import List, Any

logger = logging.getLogger(__name__)

class SubtitleExporter:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _format_timestamp(self, seconds: float) -> str:
        """Converte segundos em formato de timestamp SRT (HH:MM:SS,mmm)."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        milliseconds = int(round((seconds - int(seconds)) * 1000))
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

    def export_srt(self, segments: List[Any], filename: str = "subtitle.srt") -> str:
        """
        Exporta uma lista de segmentos do whisper para um arquivo .srt.
        Retorna o caminho completo para o arquivo gerado.
        """
        output_path = self.output_dir / filename
        logger.info(f"Gerando arquivo de legenda em: {output_path}")

        try:
            srt_content = []
            for i, segment in enumerate(segments, start=1):
                start_str = self._format_timestamp(segment.start)
                end_str = self._format_timestamp(segment.end)
                text = segment.text.strip()

                srt_content.append(f"{i}\n{start_str} --> {end_str}\n{text}\n")

            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(srt_content))

            logger.info("Arquivo SRT gerado com sucesso.")
            return str(output_path)
        except Exception as e:
            logger.error(f"Erro ao exportar arquivo SRT: {e}")
            raise RuntimeError(f"Falha na exportação de legendas: {e}")
