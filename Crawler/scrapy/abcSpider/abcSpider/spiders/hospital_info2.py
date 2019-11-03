# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


class Hosinfo_Spider(CrawlSpider):
	name="hosinfo"
	allowed_domains = ["webcache.googleusercontent.com","www.a-hospital.com"]
	start_urls = ['http://webcache.googleusercontent.com/search?q=cache:www.a-hospital.com/w/%25E5%2585%25A8%25E5%259B%25BD%25E5%258C%25BB%25E9%2599%25A2%25E5%2588%2597%25E8%25A1%25A8+&cd=1&hl=zh-CN&ct=clnk&gl=cn',]

	rules = (
		Rule(SgmlLinkExtractor(allow=['/w/.{0,200}%E5%8C%BB%E9%99%A2', ]), follow=True,process_links='link_filtering'),
		Rule(SgmlLinkExtractor(allow=['/w/.{0,200}%E5%88%97%E8%A1%A8', ]), follow=True,process_links='link_filtering'),
		Rule(SgmlLinkExtractor(allow=['/search.{0,100}/w/.{0,200}%E5%8C%BB%E9%99%A2', ]), follow=True,callback= 'parse_hos'),
		Rule(SgmlLinkExtractor(allow=['/search.{0,100}/w/.{0,200}%E5%88%97%E8%A1%A8', ]), follow=True),
		)


	def __init__(self,  *a,  **kwargs):
		super(Hosinfo_Spider, self).__init__(*a, **kwargs)
		self.count = 0
		self.outf = open('hos_info.txt','a')


	def link_filtering(self, links):
		ret = []
		for link in links:
			link_str = link.url[7:]
			link_str = 'http://webcache.googleusercontent.com/search?q=cache:' + link_str
			link.url = link_str
			ret.append(link)
		return ret


	def parse_hos(self,response):
		sel = response.selector

		hos_name = ''.join(sel.xpath('//*[@id="firstHeading"]/text()').extract())
		if hos_name[-2:] != u'医院':
			return
		hos_address = ''.join(sel.xpath('//*[@id="bodyContent"]/ul[1]/li[1]/text()').extract())[1:]
		if hos_address == u'':
			return
		hos_tel = ''.join(sel.xpath('//*[@id="bodyContent"]/ul[1]/li[2]/text()').extract())[1:]
		if hos_tel == u'':
			return
		hos_level = ''.join(sel.xpath('//*[@id="bodyContent"]/ul[1]/li[3]/a/text()').extract())
		hos_website = ''.join(sel.xpath('//*[@id="bodyContent"]/ul[1]/li[10]/a/text()').extract())

		hos_living_style = ''.join(sel.xpath('//*[@id="bodyContent"]/ul[1]/li[6]/a/text()').extract())

		self.outf.write(hos_name+u'\t'+hos_address+u'\t'+hos_tel+u'\t'+hos_level+u'\t'+hos_website+u'\t'+hos_living_style+u'\n')

		self.count +=1
		if self.count %10 == 0:
			self.outf.flush()




