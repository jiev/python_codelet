#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

import sys
reload(sys)
sys.setdefaultencoding(u"utf-8")

if __name__ == '__main__':
	file_to_search = open(u"./wOnly.log","r")
	lines = file_to_search.readlines()

	browser = webdriver.Chrome()
	browser.set_page_load_timeout(5)
	browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
	query_box = browser.find_element(u"id",u"query")
	search_icon = browser.find_element(u"id",u"tags_search")
	bus_icon = browser.find_element(u"id",u"tags_bus")

	lines_count = len(lines) - 1
	count = 0
	while count < 10000 :
		count += 1
		index = random.randint(0,lines_count)
		string_to_query = ' '.join(lines[index].strip().split(' ')[1:])
		
		query_box.send_keys(unicode(string_to_query,u"utf-8"))
		query_box.send_keys(Keys.RETURN)
		
		time.sleep(1)
		try:
			search_icon.click()
		except:
			browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
			query_box = browser.find_element(u"id",u"query")
			search_icon = browser.find_element(u"id",u"tags_search")

		query_box.clear()


		query_box.send_keys(unicode(string_to_query,u"utf-8"))
		query_box.send_keys(Keys.RETURN)
		time.sleep(1)
		try:
			search_icon.click()
		except:
			browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
			query_box = browser.find_element(u"id",u"query")
			search_icon = browser.find_element(u"id",u"tags_search")

		query_box.clear()

		
