import unittest
from calc.operations import add, subtract

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
