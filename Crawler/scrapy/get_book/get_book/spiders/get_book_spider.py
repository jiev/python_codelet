import scrapy
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector


class Get_Book_Spider(scrapy.Spider):
	name="get_book_spider"   
	#this name shouldn't be the same as the project name
	allowed_domains = ["read.jd.com"]
	start_urls = ['http://read.jd.com/12052/570482.html',]

	f = open('book.txt','w')


	def parse(self,response):
		sel = Selector(response)
		self.parse_content(response)

		if response.url == self.start_urls[0]:
			self.f.write('<html xmlns="http://www.w3.org/1999/xhtml" style="">')
			head_content = sel.xpath('/html/head').extract()[0]
			self.f.write(head_content.encode('utf-8'))
			self.f.write('<body>')
		try:
			next_pg_url = sel.xpath("//a[@id='read-next']/@href").extract()[0]
		except:
			return
		yield Request(next_pg_url,self.parse)



	def parse_content(self,response):
		sel = Selector(response)
		text_div = sel.xpath("//div[@id='zoom']").extract()[0]
		self.f.write(text_div.encode('utf-8'))



