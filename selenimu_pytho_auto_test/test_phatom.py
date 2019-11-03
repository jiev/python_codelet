#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

import sys
reload(sys)
sys.setdefaultencoding(u"utf-8")

if __name__ == '__main__':

	browser = webdriver.Chrome()
	browser.set_page_load_timeout(5)
	browser.get(u'https://www.sogou.com/')

	for i in range(0,10):
		time.sleep(1)
		browser.get(u'https://www.sogou.com/')



	browser.quit()
	browser = webdriver.Chrome()
	time.sleep(2)
	browser.get(u'https://www.sogou.com/')




		
