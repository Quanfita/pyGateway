from unittest import TestCase
from app import create_app, db
import json

class UserTestCase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.db = db

        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.drop_all()

    def test_get_users(self):
        res = self.client().get('/api/user/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data, [])

    def test_get_user(self):
        res = self.client().get('/api/user/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'User not found')
