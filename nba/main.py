# -*- coding: utf-8 -*- 
'''
Created on 2015

@author: diwang
'''
from scrapy import cmdline    
#cmdline.execute("scrapy crawl nba_lottery -o nba-data.csv -t csv".split())
#cmdline.execute("scrapy shell \"http:\vip.win007.com\betfa\odds.aspx?date=2015-11-04\"".split())
cmdline.execute("scrapy crawl nba_lottery -o nba-data.csv -t csv".split())