#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector


class TrvInfoSpider(CrawlSpider):
	name="travel_info"
	allowed_domains = ['www.meet99.com']
	start_urls = ['http://www.meet99.com/lvyou',]

	out_file = open('travel_info.txt','w')

	rules = (
		Rule(LinkExtractor(allow=[r'/lvyou-\w{2,40}\.html', ]), follow=True),
		Rule(LinkExtractor(allow=[r'/jingdian-\w{2,40}\.html', ]), follow=False,callback='parse_info')
		)

	def __init__(self,  *a,  **kwargs):
		super(TrvInfoSpider, self).__init__(*a, **kwargs)

	def parse_info(self,response):
		sel = Selector(response)

		trv_name = ''.join(sel.xpath('//*[@id="pageLocation"]/div[1]/text()[4]').extract())
		trv_name = trv_name.split('旅游攻略')[0]

		res_body = response.body
		if not '<h2>景区资质：</h2>' in res_body:
			return
		if not '<h2>景区简介：</h2>' in res_body:
			return
		contents_level = res_body.split('<h2>景区资质：</h2>',1)[1]
		trv_level = contents_level.split('<h2>',1)[0].strip()

		contents_detail = res_body.split('<h2>景区简介：</h2>',1)[1]
		trv_detail = contents_detail.split('<h2>',1)[0].strip()

		self.out_file.write(trv_name + '\t' + trv_level + '\t' + trv_detail + '\n')



