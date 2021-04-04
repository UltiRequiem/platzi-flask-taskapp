from flask_testing import TestCase
from flask import current_app, url_for
from keep_alive import app

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
        self.assertRedirects(self.client.get(url_for('index')), url_for('zero'))

    def test_zero_get(self):
        self.assert200(self.client.get(url_for('zero')))

    def test_zero_post(self):
        response = self.client.post(url_for('zero'))
        self.assertTrue(response.status_code, 405)

    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        self.assert200(self.client.get(url_for('auth.login')))
    
    def test_aut_login_template(self):
        self.client.get(url_for('auth.login'))
        self.assertTemplateUsed('login.html')

    def test_auth_login_post(self):
        self.assertRedirects(self.client.post(url_for('auth.login'), data={'username': 'fake_username', 'password': 'fake_password'}),url_for('index'))
