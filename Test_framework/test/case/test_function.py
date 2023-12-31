import sys, os, logging
# print(sys.path)
sys.path.append(os.getcwd())
import time
import unittest  # 單元測試模塊
from selenium import webdriver  # 引入瀏覽器驅動
from selenium.webdriver.common.by import By  # 引入xpath查找模塊
from Test_framework.utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger # 引入日志模塊
from utils.file_reader import ExcelReader  # 引入xls讀取模塊
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from utils.assertion import assertHTTPCode
from Test_framework.test.page.milelens_result_page import MilelensLoginPage, MilelensResultPage
from Test_framework.test.page.milelens_main_page import MilelensMainPage
from Test_framework.test.page.milelens_product_analysis_page import MilelensProductAnalysisPage

class TestMilelens_0(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/milelens.xlsx'

    def sub_setUp(self):
        # 初始頁面是Milelens Login page，傳入瀏覽器類型打開瀏覽器
        self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)

    def sub_tearDown(self):
        pass

    def test_search(self):
        datas = ExcelReader(self.excel).data
        # for d in datas:
        #     with self.subTest(data=d):
        self.sub_setUp()
        self.page.login('kson02@mailnesia.com', 'Pass1234')   #回推到22行 self.page = MilelensLoginPage(browser_type='chrome').get(self.URL, maximize_window=True)
        time.sleep(1)

        print('驗證彈窗的每個連結的功能')
        self.page = MilelensMainPage(self.page)
        self.page.popup()

        print('頁面跳轉到競品分析頁處理競品')
        self.page = MilelensProductAnalysisPage(self.page)
        self.page.deleteProductList()
        keywords = self.page.enterKeywordsAndAdd()
        print('keyword:' + str(keywords))

        print('回到首頁檢查與競品比較的項目是否有在裡面')
        self.page = MilelensMainPage(self.page)
        self.page.checkFanPageList(keywords)

        print('驗證粉專的貼文的縮圖是否有顯示')
        self.page = MilelensMainPage(self.page)
        self.page.myFanPageCheckFanpagePostPic()


        # self.page = MilelensResultPage(self.page)  # 頁面跳轉到result page
        # links = self.page.result_links
        # for link in links:
        #     logger.info(link.text)
        # self.sub_tearDown()

if __name__ == '__main__':
    unittest.main()

    # e = Email(title='百度搜索測試報告',
    #           message='這是今天的測試報告，請查收！',
    #           receiver='...',
    #           server='...',
    #           sender='...',
    #           password='...',
    #           path=report
    #           )
    # e.send()