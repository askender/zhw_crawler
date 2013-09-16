from scrapy.exceptions import DropItem
from zhw_crawler.utils import import_class
from zhw_crawler.settings import CONFIG_PATH


class FilterPipeline(object):

    def process_item(self, item, spider):
        spider_name = spider.name.replace('_local', '')
        import_str = '%s.%s_conf.MUST_LIST' % (CONFIG_PATH, spider_name)
        must_list = import_class(import_str)
        for i in must_list:
            if not item[i]:
                raise DropItem(
                    "Drop the item which contain empty value of %s" %
                    i)
        return item
