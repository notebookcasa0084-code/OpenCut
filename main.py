import argparse
import logging
import sys
from opencut.audio_extractor import AudioExtractor
from opencut.audio_transcriber import AudioTranscriber
from opencut.subtitle_exporter import SubtitleExporter

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s:%(funcName)s:%(lineno)d] - %(message)s"
)
logger = logging.getLogger("opencut")

def main():
    parser = argparse.ArgumentParser(
        description="OpenCut - Pipeline local de áudio, transcrição e legendas com IA."
    )
    parser.add_argument("video_path", type=str, help="Caminho para o arquivo de vídeo de entrada.")
    parser.add_argument("--model", type=str, default="base", help="Tamanho do modelo whisper (tiny, base, small, medium, large).")
    parser.add_argument("--device", type=str, default="cpu", help="Dispositivo de execução (cpu, cuda).")
    parser.add_argument("--output-dir", type=str, default="output", help="Diretório de saída para as legendas SRT.")
    parser.add_argument("--temp-dir", type=str, default="temp", help="Diretório temporário para arquivos de áudio extraídos.")

    args = parser.parse_args()

    try:
        logger.info("Iniciando pipeline integrado do OpenCut...")

        # 1. Extração de Áudio via FFmpeg
        extractor = AudioExtractor(output_dir=args.temp_dir)
        audio_path = extractor.extract_audio(args.video_path, output_audio_name="track.mp3")

        # 2. Transcrição com faster-whisper
        transcriber = AudioTranscriber(model_size=args.model, device=args.device)
        logger.info(f"Iniciando transcrição para o arquivo de áudio: {audio_path}")
        segments, info = transcriber.model.transcribe(audio_path, beam_size=5)
        
        # Converte o gerador de segmentos em lista para manipulação
        segments_list = list(segments)
        logger.info(f"Transcrição concluída. Idioma detectado: {info.language} (probabilidade: {info.language_probability:.2f})")

        # 3. Exportação para Legenda SRT
        exporter = SubtitleExporter(output_dir=args.output_dir)
        srt_path = exporter.export_srt(segments_list, filename="transcript.srt")

        logger.info(f"Processo finalizado com sucesso! Legenda gerada em: {srt_path}")

    except Exception as e:
        logger.error(f"Erro fatal durante a execução do OpenCut: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
