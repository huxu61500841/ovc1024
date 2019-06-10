import unittest
from huxu.pageobejct.Community import Community
from huxu.pageobejct.utils.BasePage import BasePage


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.commty=Community()
        cls.commty.denglv("615800841@qq.com","huxu0315")

    def test_something(self):
        self.assertEqual(True,self.commty.Keyword_test())


if __name__ == '__main__':
    unittest.main()
