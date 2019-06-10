
# -*- encoding:utf-8 -*-
import unittest


from huxu.pageobejct.tongcheng_pageobejct import tongcheng
class MyTestCase(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
           cls.tong=tongcheng()
           cls.tong.denglv("615800841@qq.com","huxu0315")



    # @classmethod
    # def setUpClass(cls):


        def test_tongcheng(self):
         self.assertTrue(self.tong.Keyword_test())


if __name__ == '__main__':
    unittest.main()
