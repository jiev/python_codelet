# coding=UTF-8
import scrapy
import psycopg2
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector

from datetime import datetime

class Zhihu_user_Spider(scrapy.Spider):
	name="zhihu_user"
	allowed_domains = ["zhihu.com"]
	start_urls = ['http://www.zhihu.com/people/gaoqiele/followees',]

	data_connection = psycopg2.connect('dbname=zhihu_user user=postgres password=new_psd')
	url_connection = psycopg2.connect('dbname=zhihu_user user=postgres password=new_psd')

	patn_for_topic = re.compile(r'在(.*?)下的回答')


	def start_requests(self):
		return [FormRequest(
			"http://www.zhihu.com/",
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

		with open('aaa.html','w') as f:
			f.write(response.body)

		url_cur.close()

	def is_link_fresh(self,cursor,link_str):
		cursor.execute("SELECT url FROM processed_url WHERE url='"+link_str+"'")
		if len(cursor.fetchall() ) == 0:
			return True
		else:
			return False

	def parse_info(self,response):
		yield Request(response.url+r'/followers',callback = self.parse)
		yield Request(response.url+r'/followees',callback = self.parse)
		sel = Selector(response)

		_id = response.url.split('/')[-1]
		url = response.url
		user_name = ''.join(sel.xpath("//div[@class='title-section ellipsis']/span[@class='name']/text()").extract())
		sex = ''.join(sel.xpath("//span[@class='item gender']/i/@class").extract()).replace("icon icon-profile-","")
		location = ''.join(sel.xpath("//span[@class='location item']/@title").extract())
		industry = ''.join(sel.xpath("//span[@class='business item']/@title").extract())
		company = ''.join(sel.xpath("//span[@class='employment item']/@title").extract())
		job = ''.join(sel.xpath("//span[@class='position item']/@title").extract())
		school = ''.join(sel.xpath("//span[@class='education item']/@title").extract())
		major = ''.join(sel.xpath("//span[@class='education-extra item']/@title").extract())
		description = ''.join(sel.xpath("//span[@class='description unfold-item']/span/text()").extract()).strip().replace("\n",'')
		followee_num = ''.join(sel.xpath("//div[@class='zm-profile-side-following zg-clear']/a[1]/strong/text()").extract())
		follower_num = ''.join(sel.xpath("//div[@class='zm-profile-side-following zg-clear']/a[2]/strong/text()").extract())
		agree_num = ''.join(sel.xpath("//span[@class='zm-profile-header-user-agree']/strong/text()").extract())
		thank_num = ''.join(sel.xpath("//span[@class='zm-profile-header-user-thanks']/strong/text()").extract())
		ask_num = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[2]/span/text()").extract())
		answer_num = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[3]/span/text()").extract())
		article_num = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[4]/span/text()").extract())
		collect_num = ''.join(sel.xpath("//div[@class='profile-navbar clearfix']/a[5]/span/text()").extract())
		update_time = str(datetime.now())
		topic_temp = ''.join(sel.xpath("//div[@class='item']/@title").extract())
		topics = ';'.join(self.patn_for_topic.findall(topic_temp))
		command_str = "INSERT INTO zhihu_user_table VALUES('"+_id+"','"+url+"','"+user_name+"','"+sex+"','"+location+"','"+industry+"','"+company+"','"+job+"','"+\
		        	school+"','"+major+"','"+description+"',"+followee_num+","+follower_num+","+agree_num+","+\
		        	thank_num+","+ask_num+","+answer_num+","+article_num+","+collect_num+",'"+update_time+"','"+topics+"')"

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
		


