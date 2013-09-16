#!/usr/bin/python
#-*-coding:utf-8-*-
import datetime
import sys

from common.define import session_pool
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime, func, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GrabDataDianping(Base):
    __tablename__ = 'grab_data_dianping'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    dianping_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(Unicode(100), nullable=False, default=u'')
    data = Column(UnicodeText, nullable=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, nullable=False, default=func.now(),
                     onupdate=datetime.datetime.now)
    comment_update_time = Column(DateTime, nullable=False, default=func.now())


class GrabDataDaodao(Base):
    __tablename__ = 'grab_data_daodao'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    daodao_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(Unicode(100), nullable=False, default=u'')
    data = Column(UnicodeText, nullable=True)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, nullable=False, default=func.now(),
                     onupdate=datetime.datetime.now)
    comment_update_time = Column(DateTime, nullable=False, default=func.now())


def make_skip_list_via_mysql(spider_name):
    spider_db = None
    if spider_name == 'dianping':
        spider_db = GrabDataDianping
    if spider_name == 'daodao':
        spider_db = GrabDataDaodao
    if spider_db:
        with session_pool.get_conn() as session:
            query = session.query(spider_db)
            for item in query:
                print(item.dianping_id)

if __name__ == "__main__":
    make_skip_list_via_mysql(sys.argv[1])
