import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(add(2, 3), 5)

    def test_case2(self):
        self.assertEqual(add(-1, 1), 0)

    def test_case3(self):
        self.assertEqual(add(10, 15), 25)

if __name__ == "__main__":
    unittest.main()
