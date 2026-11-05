import unittest
from unittest.mock import patch, MagicMock
from opencut.audio_transcriber import AudioTranscriber

class TestAudioTranscriber(unittest.TestCase):
    
    @patch('opencut.audio_transcriber.WhisperModel')
    def test_transcribe_success(self, mock_whisper_model_class):
        mock_model_instance = mock_whisper_model_class.return_value
        
        mock_segment = MagicMock()
        mock_segment.text = "Este é um teste de transcrição de áudio."
        
        mock_info = MagicMock()
        mock_info.language = "pt"
        mock_info.language_probability = 0.98
        
        mock_model_instance.transcribe.return_value = ([mock_segment], mock_info)
        
        transcriber = AudioTranscriber(model_size="base", device="cpu")
        result = transcriber.transcribe("fake_audio.mp3")
        
        self.assertEqual(result, "Este é um teste de transcrição de áudio.")
        mock_model_instance.transcribe.assert_called_once_with("fake_audio.mp3", beam_size=5)

    @patch('opencut.audio_transcriber.WhisperModel')
    def test_transcribe_exception(self, mock_whisper_model_class):
        mock_model_instance = mock_whisper_model_class.return_value
        mock_model_instance.transcribe.side_effect = Exception("Erro ao processar arquivo")
        
        transcriber = AudioTranscriber()
        
        with self.assertRaises(Exception):
            transcriber.transcribe("corrupted_audio.mp3")

if __name__ == '__main__':
    unittest.main()
