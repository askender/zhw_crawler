
from scrapely import Scraper
s = Scraper()
url1 = 'http://movie.douban.com/subject/1292063/'
data1 = {'name': u'美丽人生 La vita è bella', 'author': u'罗伯托·贝尼尼', 'time': '1997-12-20'}
s.train(url1, data1)

url2 = 'http://movie.douban.com/subject/1291560/'
# s.scrape(url2)
data2 = {'name': u'龙猫 となりのトトロ', 'author': u'宫崎骏', 'time': '1988-04-16'}
s.train(url2, data2)

url3 = 'http://movie.douban.com/subject/1293839/'
data3 = {'name': u'罗马假日 Roman Holiday', 'author': u'威廉·惠勒', 'time': '1953-08-27'}
# s.scrape(url3)
s.train(url3, data3)

url4 = 'http://movie.douban.com/subject/1292224/'
s.scrape(url4)


from scrapely import Scraper
s = Scraper()
url1 = 'http://movie.douban.com/subject/1292063/'
data1 = {'name': u'美丽人生 La vita è bella', 'author': u'罗伯托·贝尼尼', 'time': '1997-12-20'}
s.train(url1, data1)

url4 = 'http://movie.douban.com/subject/1292224/'
s.scrape(url4)
# with open('11.txt','wb') as afile:
# 	s.tofile(afile)