#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from common.define import session_pool
from zhw_crawler.utils import import_class
from zhw_crawler.settings import CONFIG_PATH


def make_mysql_skip_list(spider_name):

    import_str = '%s.db_model_%s' % (CONFIG_PATH, spider_name)
    db_model = import_class(import_str)
    DBModel = getattr(db_model, "GrabData%s" % spider_name.capitalize())
    id_name = '%s_id' % spider_name
    if DBModel:
        with session_pool.get_conn() as session:
            query = session.query(DBModel)
            for item in query:
                print(getattr(item, id_name))

if __name__ == "__main__":
    make_mysql_skip_list(sys.argv[1])
