from unittest import TestCase
from src.appy.utils import message


class ApiTestCase(TestCase):

    def test_get_fact(self):
        fact = message.get_fact()
        self.assertTrue(isinstance(fact, str) and len(fact) > 2)
