#!/usr/bin/python
#-*-coding:utf-8-*-

import json
from common.define import session_pool
from zhw_crawler.utils import import_class
from zhw_crawler.settings import CONFIG_PATH


class MysqlStorePipeline(object):

    def process_item(self, item, spider):
        spider_name = spider.name.replace('_local', '')
        data = json.dumps(dict(item))
        import_str = '%s.db_model_%s.GrabData%s' % (
            CONFIG_PATH,
            spider_name,
            spider_name.capitalize())
        DBModel = import_class(import_str)
        shopid = int(item['shopid'])
        id_name = '%s_id' % spider_name
        shop_dict = {
            id_name: shopid,
            'name': item['title'],
            'data': data,
        }
        with session_pool.get_conn() as session:
            query = session.query(DBModel).filter(
                getattr(DBModel, id_name) == shopid)
            if query.count():
                query.update(shop_dict)
            else:
                session.execute(
                    DBModel.__table__.insert(),
                    shop_dict
                )
            session.commit()
        return item
