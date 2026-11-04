import unittest
from pathlib import Path
from config import Config
from utils.logger import setup_logger
from utils.video_processor import VideoProcessor
from utils.ai_client import OllamaClient

class TestOpenCutConfig(unittest.TestCase):
    def test_config_initialization(self):
        Config.initialize()
        self.assertTrue(Config.OUTPUT_DIR.exists())
        self.assertTrue(Config.TEMP_DIR.exists())
        self.assertEqual(Config.DEFAULT_MODEL, "qwen2.5-coder:1.5b")

class TestOpenCutLogger(unittest.TestCase):
    def test_logger_setup(self):
        logger = setup_logger("test.logger")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "test.logger")

class TestOpenCutVideoProcessor(unittest.TestCase):
    def test_video_processor_init(self):
        processor = VideoProcessor()
        self.assertIsNotNone(processor)

class TestOpenCutAIClient(unittest.TestCase):
    def test_ai_client_init(self):
        client = OllamaClient()
        self.assertEqual(client.model, Config.DEFAULT_MODEL)
        self.assertEqual(client.host, Config.OLLAMA_HOST)

if __name__ == "__main__":
    unittest.main()
