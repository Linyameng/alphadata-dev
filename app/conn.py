# -*- coding: utf-8 -*-
"""
Created on 2018/5/31

@author: xing yan
"""
from sqlalchemy import create_engine, Table
from sqlalchemy import MetaData
from sqlalchemy.sql import text, select
from sqlalchemy.exc import NoSuchTableError
from collections import OrderedDict


engine = create_engine('oracle+cx_oracle://SIT_XM122_ORDERS1:howbuy2015@192.168.220.119:1521/hbqa', echo=True)
metadata = MetaData(bind=engine)

cm_blacklist_direct = Table('cm_blacklist_direct', metadata, autoload=True)

ins = cm_blacklist_direct.insert().values(fundcode='PE0461', hboneno='000002')

ins01 = cm_blacklist_direct.insert()

ins02 = "insert into cm_blacklist_direct values (:fundcode, :hboneno)"

result = engine.execute(text(ins02), fundcode='PE0463', hboneno='000005')


print(result.is_insert)

s = select([cm_blacklist_direct])

result = engine.execute(s)

for row in result:
    print(row[cm_blacklist_direct.c.fundcode])

result.close()
