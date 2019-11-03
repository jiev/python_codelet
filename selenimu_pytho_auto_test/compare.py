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

	browser2 = webdriver.Chrome()	
	browser2.set_page_load_timeout(5)
	browser2.get(u'http://10.142.43.141:8080/index_v7dev.html')

	query_box2 = browser2.find_element(u"id",u"query")
	search_icon2 = browser2.find_element(u"id",u"tags_search")
	bus_icon2 = browser2.find_element(u"id",u"tags_bus")


	for line in file_to_search:
	
		string_to_query = line.strip()
		print 'query : ' + string_to_query.decode('utf-8')
		
		query_box.send_keys(unicode(string_to_query,u"utf-8"))
		query_box.send_keys(Keys.RETURN)
		
		time.sleep(1)
		try:
			search_icon.click()
		except:
			browser.get(u'http://10.142.43.141:8080/index_v7dev.html')
			query_box = browser.find_element(u"id",u"query")
			search_icon = browser.find_element(u"id",u"tags_search")

		raw_input('press any key to continue ...')

		query_box2.send_keys(unicode(string_to_query,u"utf-8"))
		query_box2.send_keys(Keys.RETURN)
		time.sleep(1)
		try:
			search_icon2.click()
		except:
			browser2.get(u'http://10.142.43.141:8080/index_v7dev.html')
			query_box2 = browser2.find_element(u"id",u"query")
			search_icon2 = browser2.find_element(u"id",u"tags_search")


		raw_input('press any key to continue ...')

		query_box.clear()
		query_box2.clear()

		

		
