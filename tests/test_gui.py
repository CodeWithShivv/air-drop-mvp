# Unit tests for GUI components
import unittest
from gui.main_window import MainWindow

class TestGUI(unittest.TestCase):
    def test_main_window(self):
        window = MainWindow()
        self.assertEqual(window.windowTitle(), "Airdrop-like File Transfer")

if __name__ == '__main__':
    unittest.main()
