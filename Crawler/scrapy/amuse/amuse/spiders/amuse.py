from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class AmuseSpider(CrawlSpider):
	name="amuse"
	allowed_domains = ["book.sto.cc"]
	html_base = 'http://book.sto.cc/'
	start_urls = ['http://book.sto.cc/1551-1/',]

	rules = (
		Rule(SgmlLinkExtractor(allow=['/1551-\d{1,2}/', ]), follow=True,callback='parse_artical'),
		)

	def __init__(self,  *a,  **kwargs):
		super(AmuseSpider, self).__init__(*a, **kwargs)


	def parse_start_url(self, response):
		return [self.parse_artical(response)]


	def parse_artical(self,response):
		s = response.selector
		head_content = s.xpath('/html/head').extract()
		book_content = s.xpath('//div[@id="BookContent"]').extract()

		with open('amuse ourselves to death'+response.url[-3:-1]+'.html','w') as f:
			f.write('<html xmlns="http://www.w3.org/1999/xhtml" style="">')
			f.write(head_content[0].encode('utf-8'))
			f.write('<body>')
			f.write(book_content[0].encode('utf-8'))
			f.write('</body></html>')




