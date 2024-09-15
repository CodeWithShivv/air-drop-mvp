# Unit tests for networking components
import unittest
from networking.connection import create_connection

class TestNetworking(unittest.TestCase):
    def test_create_connection(self):
        connection = create_connection('127.0.0.1', 5000)
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()
