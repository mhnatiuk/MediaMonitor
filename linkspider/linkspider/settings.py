# -*- coding: utf-8 -*-

# Scrapy settings for linkspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'linkspider'
LOG_LEVEL="INFO"
SPIDER_MODULES = ['linkspider.spiders']
NEWSPIDER_MODULE = 'linkspider.spiders'

ITEM_PIPELINES  = {'linkspider.pipelines.AgoraspiderPipeline' : 100,  }
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'linkspider/science'
