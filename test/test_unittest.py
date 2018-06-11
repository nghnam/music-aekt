import unittest
 
class TestUnitTest(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_add(self):
        self.assertEqual(5+7, 12)
 
    def test_multiply(self):
        self.assertEqual(2*2, 4)

if __name__ == '__main__':
    unittest.main()

