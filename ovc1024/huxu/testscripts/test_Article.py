import unittest
from huxu.pageobejct.Article import Article


class MyTestCase(unittest.TestCase):
    def test_something(self):


        self.assertEqual(True, Article().Keyword_test())


if __name__ == '__main__':
    unittest.main()
