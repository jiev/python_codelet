import scrapy
import psycopg2
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector

from datetime import datetime

class Zhihu_user_Spider(scrapy.Spider):
	name="zhihu_user"
	allowed_domains = ["zhihu.com"]
	start_urls = ['http://www.zhihu.com/people/jixin/followers',]

	data_connection = psycopg2.connect('dbname=zhihu_user user=postgres password=new_psd')
	url_connection = psycopg2.connect('dbname=zhihu_user user=postgres password=new_psd')


	def start_requests(self):
		return [FormRequest(
			"http://zhihu.com/login",
			formdata = {'email':'if_if_if_fi@163.com',
			'password':'password0if'
			},
			callback = self.after_login
			)]

	def after_login(self,response):
		for url in self.start_urls:
			yield self.make_requests_from_url(url)

	def parse(self,response):
		url_cur = self.url_connection.cursor()

		link_peoples = SgmlLinkExtractor(allow=[r'/people/[^/]+$', ]).extract_links(response)
		for link in link_peoples:
			if self.is_link_fresh(url_cur,link.url):
				yield Request(link.url,callback = self.parse_info)
				yield Request(link.url+r'/followers',callback = self.parse)
				yield Request(link.url+r'/followees',callback = self.parse)

		url_cur.close()

	def is_link_fresh(self,cursor,link_str):
		cursor.execute("SELECT url FROM processed_url WHERE url='"+link_str+"'")
		if len(cursor.fetchall() ) == 0:
			return True
		else:
			return False

	def parse_info(self,response):
		sel = Selector(response)
				
		user = {}
		user['id'] = response.url.split('/')[-1]
		user['url'] = response.url
		user['user_name'] = ''.join(sel.xpath("//div[@class='title-section ellipsis']/span[@class='name']/text()").extract())
		user['sex'] = ''.join(sel.xpath("//span[@class='item gender']/i/@class").extract()).replace("icon icon-profile-","")
		user['location'] = ''.join(sel.xpath("//span[@class='location item']/@title").extract())
		user['industry'] = ''.join(sel.xpath("//span[@class='business item']/@title").extract())
		user['company'] = ''.join(sel.xpath("//span[@class='employment item']/@title").extract())
		user['job'] = ''.join(sel.xpath("//span[@class='position item']/@title").extract())
		user['school'] = ''.join(sel.xpath("//span[@class='education item']/@title").extract())
		user['major'] = ''.join(sel.xpath("//span[@class='education-extra item']/@title").extract())
		user['description'] = ''.join(sel.xpath("//span[@class='description unfold-item']/span/text()").extract()).strip().replace("\n",'')
		user['followee_num'] = ''.join(sel.xpath("//div[@class='zm-profile-side-following zg-clear']/a[1]/strong/text()").extract())
		user['follower_num'] = ''.join(sel.xpath("//div[@class='zm-profile-side-following zg-clear']/a[2]/strong/text()").extract())
		user['agree_num'] = ''.join(sel.xpath("//span[@class='zm-profile-header-user-agree']/strong/text()").extract())
		user['thank_num'] = ''.join(sel.xpath("//span[@class='zm-profile-header-user-thanks']/strong/text()").extract())
		user['ask_num'] = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[2]/span/text()").extract())
		user['answer_num'] = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[3]/span/text()").extract())
		user['article_num'] = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[4]/span/text()").extract())
		user['collect_num'] = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[5]/span/text()").extract())
		user['update_time'] = str(datetime.now())
		command_str = "INSERT INTO zhihu_user_table VALUES('"+user['id']+"','"+user['url']+"','"+user['user_name']+"','"+user['sex']+"','"+user['location']+"','"+user['industry']+"','"+user['company']+"','"+user['job']+"','"+\
		        	user['school']+"','"+user['major']+"','"+user['description']+"',"+user['followee_num']+","+user['follower_num']+","+user['agree_num']+","+\
		        	user['thank_num']+","+user['ask_num']+","+user['answer_num']+","+user['article_num']+","+user['collect_num']+",'"+user['update_time']+"')"

		try:
			data_connection = psycopg2.connect('dbname=zhihu_user user=postgres password=new_psd')

			data_cur = data_connection.cursor()
			data_cur.execute("INSERT INTO processed_url (url) VALUES('"+response.url+"')")
			data_cur.execute(command_str)
			data_cur.close()
			data_connection.commit()
			data_connection.close()
		except:
			data_connection.rollback()
			data_connection.close()
			pass
		


