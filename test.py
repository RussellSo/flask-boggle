from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
app.config['TESING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):
    
    def test_home(self):
        """testing home route"""
        with app.test_client() as client:
            res = client.get('/')

            self.assertEqual(res.status_code, 200)
            self.assertIn('board', session) ## test if board is in session

    def test_valid_word(self):
        """ test a valid word - forces a word into board sesion"""

        with app.test_client() as client:
            
            with client.session_transaction() as change_session:
                change_session['board'] = [['C','A','T','T','T'],
                                           ['C','A','T','T','T'],
                                           ['C','A','T','T','T'],
                                           ['C','A','T','T','T'],
                                           ['C','A','T','T','T']]
                client.get('/')
                res = client.get('/guesses?guess=cat')
                self.assertEqual(res.json['res'], 'ok') #nonetype is not subscriptable
                # self.assertEqual(res.status_code, 200)

    def test_invalid_word(self):
        """ test if word in dictionary"""

        with app.test_client() as client:
            client.get('/') ##need this line in this case
            res = client.get('/guesses?guess=impossible')
            self.assertEqual(res.json['res'], 'not-on-board')
