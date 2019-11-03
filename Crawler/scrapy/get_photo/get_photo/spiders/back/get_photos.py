import scrapy
import urllib
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector

from datetime import datetime

class Get_Photo_Spider(scrapy.Spider):
	name="get_photos"   
	#this name shouldn't be the same as the project name
	allowed_domains = ["aomy.com"]
	start_urls = ['http://www.aomy.com/a/8/819.html',]

	patn = re.compile(r'/attach/2011-10/131949.{7,9}\.jpg')

	def parse(self,response):

		link_page = SgmlLinkExtractor(allow=[r'/a/8/819_\d.html', ]).extract_links(response)
		for link in link_page:
				yield Request(link.url,callback = self.parse)

		link_photos = self.patn.findall(response.body)

		for link in link_photos:
			self.get_photo(r'http://www.aomy.com/'+link)

	def get_photo(self,photo_url):
		urllib.urlretrieve(photo_url,'./photos/'+photo_url.split('/')[-1])

		



		


