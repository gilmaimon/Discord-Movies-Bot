import unittest

import sys
sys.path.append("../app") # Adds higher directory to python modules path.

from bot import MoviesBot

class TestMessage:
    def __init__(self, content):
        self.content = content

def is_movies_request(content):
    return MoviesBot.is_movies_request(TestMessage(content))

def get_query_from_command(content):
    return MoviesBot.get_query_from_command(TestMessage(content))

class TestStringMethods(unittest.TestCase):

    def is_movie_request(self):
        self.assertTrue(is_movies_request("!movie rush hour"))
        self.assertTrue(is_movies_request("!movies rush hour"))
        self.assertTrue(is_movies_request("!moviebot rush hour"))
        self.assertTrue(is_movies_request("!moviesbot rush hour"))
        
        self.assertFalse(is_movies_request("!moviesbot"))
        self.assertFalse(is_movies_request("!movies "))
        self.assertFalse(is_movies_request("movies rush hour"))
        self.assertFalse(is_movies_request("!titanic"))

    def get_query_from_command(self):
        self.assertEqual(get_query_from_command('!movies rush hour 1'), 'rush hour 1')
        self.assertEqual(get_query_from_command('!moviesbot titanic'), 'titanic')

if __name__ == '__main__':
    unittest.main()
