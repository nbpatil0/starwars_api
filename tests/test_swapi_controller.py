import unittest
from app import app, db

class TestSwapiController(unittest.TestCase):

    def setUp(self):
        # Set up a test Flask app and configure it
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing

        with app.app_context():
            # Initialize the test database
            db.create_all()

    def tearDown(self):
        with app.app_context():
            # Clean up the test database
            db.session.remove()
            db.drop_all()

    def test_fetch_swapi_data(self):
        with app.test_client() as client:
            response = client.get('/swapi/films')
            self.assertEqual(response.status_code, 200)
            data = response.json
            self.assertIsInstance(data, dict)
            self.assertIn('data', data)

    def test_invalid_resource(self):
        with app.test_client() as client:
            response = client.get('/swapi/invalid_resource')
            self.assertEqual(response.status_code, 400)
            self.assertIn(b'Invalid resource provided', response.data)

if __name__ == '__main__':
    unittest.main()
