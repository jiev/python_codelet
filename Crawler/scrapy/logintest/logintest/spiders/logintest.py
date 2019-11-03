from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest


class LoginTestSpider(CrawlSpider):
	name="logintest"
	allowed_domains = ["zhihu.com"]
	start_urls = ['http://www.zhihu.com/people/jixin/followers',]
	rules = (
		Rule(SgmlLinkExtractor(allow=['/people/[^/]+', ]), follow=True,callback= None),
		Rule(SgmlLinkExtractor(allow=['/people/[^/]+/followers', ]), follow=True,callback= None),
		Rule(SgmlLinkExtractor(allow=['/people/[^/]+/followees', ]), follow=True,callback= None),
		Rule(SgmlLinkExtractor(allow=['/people/[^/]+/about', ]), follow=True,callback='parse_people_info'),
		)

	def __init__(self,  *a,  **kwargs):
		super(LoginTestSpider, self).__init__(*a, **kwargs)

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
		


