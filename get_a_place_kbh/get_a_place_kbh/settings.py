# -*- coding: utf-8 -*-

# Scrapy settings for get_a_place_kbh project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'get_a_place_kbh'

SPIDER_MODULES = ['get_a_place_kbh.spiders']
NEWSPIDER_MODULE = 'get_a_place_kbh.spiders'

FEED_FORMAT='csv'
FEED_URI='findbolig.csv'
FEED_EXPORT_ENCODING = "utf-8"

import os
path = str(os.getcwd())
if 'Google Drev' in path:
    USER_AGENT_LIST = '/mnt/c/Users/ngh1a/Google Drev/Get_a_place/scrapy_useragents/useragents.txt'
elif 'server' in path:
    USER_AGENT_LIST = '/home/server/Desktop/GIT/getX/scrapy_useragents/useragents.txt'
elif 'Desktop' in path:
    USER_AGENT_LIST = '/home/dennis/Desktop/getX/scrapy_useragents/useragents.txt'
else:
    USER_AGENT_LIST = '/mnt/c/Users/ngh1a/Google Drive/Get_a_place/scrapy_useragents/useragents.txt'




# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'get_a_place_kbh (+http://www.yourdomain.com)'

DOWNLOADER_MIDDLEWARES = {
    #scrapy
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    #random-user-agent
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'random_useragent.RandomUserAgentMiddleware': 400,
}


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'get_a_place_kbh.middlewares.GetAPlaceKbhSpiderMiddleware': 543,
#}

#scrapy_splash cache
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

COOKIES_ENABLED = True

HTTPERROR_ALLOW_ALL = True

DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 5
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

