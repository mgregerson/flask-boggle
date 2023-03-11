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
    

            # Tests for a 200 status code - OK!
            self.assertEqual(response.status_code, 200)
            # Tests that the length of the board is five
            self.assertEqual((len(html_dict['board'])), 5)
            # Tests that it returns a game id
            self.assertIn(html_dict['game_id'], html_dict.values())
            # Tests that game_id is a string
            self.assertEqual(type(html_dict['game_id']), str)
            # Check that the board is a list of lists
            self.assertEqual(type(html_dict['board'][0]), list)
            self.assertEqual(type(html_dict['board'][1]), list)
            self.assertEqual(type(html_dict['board'][2]), list)
            self.assertEqual(type(html_dict['board'][3]), list)
            self.assertEqual(type(html_dict['board'][4]), list)
            # Check that the games dictionary includes 
            self.assertIn(html_dict['game_id'], games)


            print(len(html_dict['board']), html_dict['game_id'])
            print(html_dict.values())


#    def is_all_lists(list):
#         for line in list:
#             if (line != type(list)):
#                 return False
#             else:
#                 return True