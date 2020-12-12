import unittest
from models import Department, Employee
from app import app, db

SQLALCHEMY_DATABASE_URI = "sqlite://test.db"
TESTING = True

class TestViews(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()


    def tearDown(self):
        pass

    def test_index(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code, 200)
        # self.assertEqual(render_tempate.name, 'index.html')


if __name__ == '__main__':
    unittest.main()