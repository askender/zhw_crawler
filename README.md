zhw_crawler
===========

找好玩-爬虫


This is a Scrapy project to scrape websites for information...
And try to be a common framework to scrape websites.

[zhw_crawler html5-slide幻灯片](http://blog.askender.com/slides/zhw_crawler/)

This project contains spiders that you can see by running:

    scrapy list

You can debug xpath by: `scrapy shell http://www.dianping.com/shop/500883`


Update proxies(It will auto update when spider running):

    python zhw_crawler/conf/update_proxies.py

Use:

    scrapy crawl dianping
    scrapy crawl dianping_local

Make skip list from db or html for next run:

    python zhw_crawler/commands/make_skiplist_via_mysql.py dianping > zhw_crawler/log/dianping/skip.txt
    python zhw_crawler/commands/make_skiplist_via_html.py daodao > zhw_crawler/log/daodao/skip.txt

A simple check:

    http://localhost:6080/enginestatus

Use Scrapyd:

    scrapyd-deploy -l
    scrapyd-deploy -L zhw_crawler1
    scrapyd-deploy zhw_crawler1 -p default
    scrapyd-deploy zhw_crawler1 -p zhw_crawler_alpha
    scrapyd-deploy zhw_crawler1 -p zhw_crawler_alpha --version f864be
    curl http://localhost:6800/schedule.json -d project=zhw_crawler_alpha -d spider=dainping
    curl http://localhost:6800/schedule.json -d project=zhw_crawler_alpha -d spider=doubanmovie_local

Thanks [【找好玩】华东地区最全面的周末旅游攻略信息指南](http://zhaohaowan.com/) I am working on, which make this become a open-source project.
