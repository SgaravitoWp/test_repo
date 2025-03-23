from unittest import TestCase
from src.biyection import wordPattern

class TestBiyection(TestCase):

    def test_result(self):
        self.assertFalse(wordPattern("jquery", "jquery"))