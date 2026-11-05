import unittest
from unittest.mock import MagicMock, mock_open, patch
from opencut.subtitle_exporter import SubtitleExporter

class TestSubtitleExporter(unittest.TestCase):

    def test_format_timestamp(self):
        exporter = SubtitleExporter()
        self.assertEqual(exporter._format_timestamp(0.0), "00:00:00,000")
        self.assertEqual(exporter._format_timestamp(65.5), "00:01:05,500")
        self.assertEqual(exporter._format_timestamp(3661.125), "01:01:01,125")

    @patch('builtins.open', new_callable=mock_open)
    def test_export_srt_success(self, mock_file):
        seg1 = MagicMock(start=0.0, end=2.5, text="Olá mundo")
        seg2 = MagicMock(start=3.0, end=5.2, text="Teste de legenda")
        
        exporter = SubtitleExporter(output_dir="output")
        output_path = exporter.export_srt([seg1, seg2], "test.srt")
        
        self.assertTrue(output_path.endswith("test.srt"))
        mock_file.assert_called_once()
        
        # Verifica se o conteúdo gerado contém os timestamps corretos
        handle = mock_file()
        written_data = "".join(call.args[0] for call in handle.write.mock_calls)
        self.assertIn("00:00:00,000 --> 00:00:02,500", written_data)
        self.assertIn("Olá mundo", written_data)
        self.assertIn("00:00:03,000 --> 00:00:05,200", written_data)
        self.assertIn("Teste de legenda", written_data)

if __name__ == '__main__':
    unittest.main()
