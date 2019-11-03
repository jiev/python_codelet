#encoding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

import sys
reload(sys)
sys.setdefaultencoding(u"utf-8")

if __name__ == '__main__':
	file_to_search = open(sys.argv[1])

	browser = webdriver.Chrome()	
	browser.set_page_load_timeout(5)
	browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
	
	query_box = browser.find_element(u"id",u"query")
	search_icon = browser.find_element(u"id",u"tags_search")
	bus_icon = browser.find_element(u"id",u"tags_bus")

	count = 0
	for line in file_to_search:
	
		string_to_query = unicode(line.strip(),u"utf-8")
		count += 1
		print unicode(count) + '\t' + 'query : ' + string_to_query
		
		query_box.send_keys(string_to_query)
		query_box.send_keys(Keys.RETURN)
		
		time.sleep(1)
		try:
			search_icon.click()
		except:
			browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
			query_box = browser.find_element(u"id",u"query")
			search_icon = browser.find_element(u"id",u"tags_search")

		query_box.clear()
	
