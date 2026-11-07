import unittest
from src.greetings import hello


class TestGreetings(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello("Мир"), "Привет, Мир!")

    def test_empty(self):
        self.assertEqual(hello(""), "Привет, !")


if __name__ == "__main__":
    unittest.main()
