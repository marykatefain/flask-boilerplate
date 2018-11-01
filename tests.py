import unittest
from server import app


class TestClass(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    # Test that the app returns 200
    def test_index_is_200(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Test that the index returns the proper data
    def test_index_repsonse_content(self):
        response = self.app.get('/')
        self.assertIn(b'hello world', response.data)


if __name__ == '__main__':
    unittest.main()
