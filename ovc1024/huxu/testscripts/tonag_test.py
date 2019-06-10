import unittest
from huxu.pageobejct.tonag import TOnag


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, TOnag().Keyword_test())


if __name__ == '__main__':
    unittest.main()
