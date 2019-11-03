# -*- coding: utf-8 -*-

# Scrapy settings for get_photo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'get_photo'

SPIDER_MODULES = ['get_photo.spiders']
NEWSPIDER_MODULE = 'get_photo.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = './photos'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'get_photo (+http://www.yourdomain.com)'
