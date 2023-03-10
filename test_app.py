from unittest import TestCase

from flask import jsonify, json

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:

            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('id="start-button"', html)
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            # the route returns JSON with a string game id, and a list-of-lists for the board
            # the route stores the new game in the games dictionary
            response = client.post('/api/new-game')
            html = response.get_data(as_text=True)
            html_dict = json.loads(html)

            self.assertEqual(response.status_code, 200)
            print(response.is_json)
