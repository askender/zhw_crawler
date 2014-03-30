import datetime
from sqlalchemy import Column, Integer
from sqlalchemy import DateTime, func, Unicode, UnicodeText
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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
