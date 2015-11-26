#--encoding:utf-8--
# Scrapy settings for nba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nba'

SPIDER_MODULES = ['nba.spiders']
NEWSPIDER_MODULE = 'nba.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nba (+http://www.yourdomain.com)'


# liansai.500.com domain config
LP = "215"    # 2013/2014:177    2014/2015:215
PROC = "1172"  # 2013/2014:980    2014/2015:1172
SEASON = 2015  # 2013/2014:2013   2014/2015:2014

# odds spider config
PLAYID = "313"  #娣峰悎杩囧叧:313    璁╁垎鑳滆礋:275
PERIOD = 1   #瀹氫箟鐖彇鏈�杩慞ERIOD澶╃殑鍘嗗彶璧旂巼鏁版嵁

