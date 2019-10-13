# -*- coding: utf-8 -*-
import sys
import time

from scrapy.http import HtmlResponse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from .settings import START_URLS


# Chrome Driverの実行オプションを設定
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
# chrome_options.binary_location = '/Applications/Google Chrome.app'

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/ubuntu/scraping/scrapy_myproject/myproject/chromedriver')
# /Users/plus/chromedriver
# /Users/user/chromedriver

class SeleniumMiddleware(object):
    
    def process_request(self, request, spider):  
        #ページ読み込み
        driver.get(request.url)
        print(START_URLS)
        #一覧ページに対するrequestの場合のみSeleniumMiddlewareを使う
        if request.url in START_URLS:
          while True:
            driver.execute_script('scroll(0, document.body.scrollHeight)')
            time.sleep(1)

            # loaderが見えなくなったら終了
            element = driver.find_element_by_class_name("vod-mod-loader")
          
            if not element.is_displayed():
              break

        return HtmlResponse(
            driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request
        )
        
def close_driver():
  driver.close()