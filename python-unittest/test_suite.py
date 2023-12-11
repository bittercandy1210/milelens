import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]   # 新增測試用例列表
    suite.addTests(tests)   # 將測試用例清單新增至測試組中
    suite.addTest(TestMathFunc("test_multi"))  # 直接用addTest方法添加單個TestCase
    # 用addTests + TestLoader。不過用TestLoader的方法是無法對case進行排序的
    # loadTestsFromName()，傳入'模塊名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，類似，傳入列表

    # loadTestsFromTestCase()，傳入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # suite中也可以套suite

    # 將測試結果輸出到測試報告中
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # 將測試結果輸出到測試報告html中
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)

    # 直接將結果輸出到控制台
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
