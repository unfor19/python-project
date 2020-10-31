from unittest import TestCase, mock
from io import StringIO
from src.appy.core import app


class GreetTestCase(TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_fullname(self, mock_stdout):
        with mock.patch('builtins.input', return_value="meir gabay"):
            app.main()
            self.assertTrue(
                'Hello Meir Gabay' in mock_stdout.getvalue()
            )

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_firstname(self, mock_stdout):
        with mock.patch('builtins.input', return_value="meir"):
            app.main()
            self.assertTrue(
                'Hello Meir' in mock_stdout.getvalue()
            )

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_number(self, mock_stdout):
        with mock.patch('builtins.input', return_value="123"):
            app.main()
            self.assertTrue(
                'Hello 123' in mock_stdout.getvalue()
            )
