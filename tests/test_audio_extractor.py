import unittest
from unittest.mock import patch, MagicMock
from opencut.audio_extractor import AudioExtractor

class TestAudioExtractor(unittest.TestCase):
    
    @patch('opencut.audio_extractor.subprocess.run')
    @patch('opencut.audio_extractor.os.path.exists')
    def test_extract_audio_success(self, mock_exists, mock_subprocess_run):
        # Simula que o arquivo de vídeo existe
        mock_exists.return_value = True
        
        # Simula sucesso na execução do subprocess
        mock_subprocess_run.return_value = MagicMock(returncode=0)
        
        extractor = AudioExtractor(output_dir="temp")
        output_path = extractor.extract_audio("fake_video.mp4", "test_audio.mp3")
        
        self.assertTrue(output_path.endswith("test_audio.mp3"))
        mock_subprocess_run.assert_called_once()

    @patch('opencut.audio_extractor.os.path.exists')
    def test_extract_audio_file_not_found(self, mock_exists):
        # Simula que o arquivo de vídeo NÃO existe
        mock_exists.return_value = False
        
        extractor = AudioExtractor()
        with self.assertRaises(FileNotFoundError):
            extractor.extract_audio("nonexistent.mp4")

if __name__ == '__main__':
    unittest.main()
