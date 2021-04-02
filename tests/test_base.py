from flask_testing import TestCase
from flask import current_app, url_for
from .main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))

        self.assertRedirects(response, url_for('zero'))

    def test_zero_get(self):
        response = self.client.get(url_for('zero'))

        self.assert200(response)

    def test_hello_post(self):
        fake_form = {
                'username':'fake_user',
                'password':'fake_password'
                }

        response = self.client.post(url_for('zero'), data=fake_form)

        self.assertRedirects(response, url_for('index'))

    def test_auth_blueprint_exists(self):
         self.assertIn('auth',self.app.blueprints)


