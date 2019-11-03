# -*- coding: utf-8 -*-

# Scrapy settings for Hos_Info project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Hos_Info'

SPIDER_MODULES = ['Hos_Info.spiders']
NEWSPIDER_MODULE = 'Hos_Info.spiders'


RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_DELAY = 0.5

SPIDER_MIDDLEWARES = {
    'Hos_Info.middlewares.ProxyMiddleware': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Hos_Info (+http://www.yourdomain.com)'
