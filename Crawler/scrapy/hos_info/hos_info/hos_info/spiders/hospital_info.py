﻿# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from datetime import datetime

class Hosinfo_Spider(CrawlSpider):
	name="hosinfo"
	allowed_domains = ["www.a-hospital.com"]
	start_urls = ['http://www.a-hospital.com%2fw%2f%e9%82%b5%e9%98%b3%e5%b8%82%e5%8c%bb%e9%99%a2%e5%88%97%e8%a1%a8',]

	rules = (
		Rule(SgmlLinkExtractor(allow=['/w/.{0,200}%E5%8C%BB%E9%99%A2', ]), follow=True,callback='parse_hos'),
		Rule(SgmlLinkExtractor(allow=['/w/.{0,200}%E5%88%97%E8%A1%A8', ]), follow=True,callback=None),
		)

	def __init__(self,  *a,  **kwargs):
		super(Hosinfo_Spider, self).__init__(*a, **kwargs)
		self.count = 0
		self.outf = open('hos_info.txt','a')


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
		self.outf.flush()


