# -*- coding: utf-8 -*-

# Scrapy settings for hos_info project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hos_info'

SPIDER_MODULES = ['hos_info.spiders']
NEWSPIDER_MODULE = 'hos_info.spiders'

RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 1.0

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'hos_info.middlewares.ProxyMiddleware': 800,
} 

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hos_info (+http://www.yourdomain.com)'
