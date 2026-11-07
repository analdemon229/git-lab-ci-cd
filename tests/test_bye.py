import unittest
from src.greetings import bye


class TestBye(unittest.TestCase):

    def test_bye(self):
        self.assertEqual(bye("Мир"), "Пока, Мир!")


if __name__ == "__main__":
    unittest.main()
