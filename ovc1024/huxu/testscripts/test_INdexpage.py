# -*- encoding:utf-8 -*-
import unittest
from huxu.pageobejct.IndexPage import INdexPage


class MyTestCase(unittest.TestCase):
    def test_something(self):


        self.assertEqual(True,INdexPage().Keyword_test())


if __name__ == '__main__':
    unittest.main()
